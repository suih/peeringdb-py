
import urllib2
import json
import time
from redis import Redis

class PeeringDB:

    cache_enable = None
    cache_ttl = None
    cache_prefix = None
    redis = None

    def __init__(self, cache=True, cache_ttl=900, cache_prefix="peeringdb", cache_host="localhost", cache_port=6379, cache_db=0):
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
            print key
            data = self.redis.get(key)
            if data is None:
                data = self.pdb_getsrc(param)
                p = self.redis.pipeline()
                p.set(key, data)
                p.expireat(key, int(time.time()) + self.cache_ttl)
                p.execute()
        return json.loads(data)["data"][0]


    def pdb_getsrc(self, param):
        url = "https://beta.peeringdb.com/api/%s" % (param)
        resp = urllib2.urlopen(url)
        return resp.read()

    def asn(self, asn):
        return self.pdb_get("asn/%s" % (asn))

    def ixlan(self, ixlanid):
        return self.pdb_get("ixlan/%s" % (ixlanid))

    def ix(self, ixid):
        return self.pdb_get("ix/%s" % (ixid))
