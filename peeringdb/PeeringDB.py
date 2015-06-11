# Copyright 2015 Netflix. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import urllib2
import json
import time
from redis import Redis


class PeeringDB:

    cache_enable = None
    cache_ttl = None
    cache_prefix = None
    redis = None

    def __init__(self, cache=True, cache_ttl=900, cache_prefix="peeringdb",
                 cache_host="localhost", cache_port=6379, cache_db=0):
        self.cache_enable = cache
        self.cache_ttl = cache_ttl
        self.cache_prefix = cache_prefix
        self.redis = Redis(host=cache_host, port=cache_port, db=cache_db)
        return

    def pdb_get(self, param, cache=True):
        if cache is False or self.cache_enable is False:
            # no caching
            data = self.pdb_getsrc(param)
        else:
            # caching
            key = "%s_%s" % (self.cache_prefix, param)
            data = self.redis.get(key)
            if data is None:
                data = self.pdb_getsrc(param)
                p = self.redis.pipeline()
                p.set(key, data)
                p.expireat(key, int(time.time()) + self.cache_ttl)
                p.execute()
        return json.loads(data)["data"][0]

    def pdb_getsrc(self, param):
        agent = "peeringdb-py"
        url = "https://beta.peeringdb.com/api/%s" % (param)
        resp = urllib2.urlopen(url)
        return resp.read()

    def get_obj(self, type, id):

        return self.pdb_get("%s/%s" % (type, id))

    # base objects

    def asn(self, asn):
        return self.get_obj("asn", asn)

    def fac(self, facid):
        return self.get_obj("fac", facid)

    def ixlan(self, ixlanid):
        return self.get_obj("ixlan", ixlanid)

    def ix(self, ixid):
        return self.get_obj("ix", ixid)

    def net(self, netid):
        return self.get_obj("net", netid)

    def org(self, orgid):
        return self.get_id("org", orgid)

    def poc(self, pocid):
        return self.get_id("poc", pocid)

    # helpers

    def matching_facility(self, asnnums):

        asns = {}
        facility_all = {}
        for asnnum in asnnums:
            asn = self.asn(asnnum)
            asns[asnnum] = asn
            for facility in asn["facility_set"]:
                facilityid = facility["facility"]
                if facility not in facility_all:
                    facility_all[facility] = None

        facility_match = []
        return facility_match

    def matching_ixlan(self, asnnums):

        asns = {}
        asn_ixlans = {}
        ixlan_all = {}
        ixlan_match = []

        # get asn details
        for asnnum in asnnums:
            asn = self.asn(asnnum)
            asns[asnnum] = asn
            asn_ixlans[asnnum] = []
            # get ixlans for each asn
            for link in asn["ixlink_set"]:
                ixlan_id = link["ix_lan"]
                asn_ixlans[asnnum].append(ixlan_id)
                if ixlan_id not in ixlan_all:
                    ixlan_all[ixlan_id] = None

        # look for matches
        for ixlan in ixlan_all:
            occurs = 0
            for asn in asns:
                if ixlan in asn_ixlans[asn]:
                    occurs = occurs + 1
            ixlan_all[ixlan] = occurs
            if occurs == len(asnnums):
                ixlan_obj = self.ixlan(ixlan)
                # grab ix object too
                ixlan_obj["ix_obj"] = self.ix(ixlan_obj["ix"])
                ixlan_obj["links"] = self.get_ixlanlinks(asns[asn], ixlan)
                ixlan_match.append(ixlan_obj)

        return ixlan_match


    def get_ixlanlinks(self, asn, ixlan_id):
        links = []
        for link in asn["ixlink_set"]:
            if link["ix_lan"] == ixlan_id:
                links.append(link)
        return links
