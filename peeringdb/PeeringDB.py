
import urllib2
import json
import time
from redis import Redis

class PeeringDB:

    cache_enable = None
    cache_ttl = None
    redis = Redis()

    def __init__(self, cache=True, cache_ttl = 300):
        self.cache_enable = cache
        self.cache_ttl = cache_ttl
        return


    def pdb_get(self, param, cache=True):
        if cache is False or self.cache_enable is False:
            # no caching
            data = self.pdb_getsrc(param)
        else:
            # caching
            key = "peerindb_%s" % (param)
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
