# _*_coding=utf-8 _*_
# @author zhangsanga
# @date 2020/11/4 16:17


from app.config.test_config import config_file
import threading
import redis
import sys

sys.path.append('../../../')


class RedisTool(object):
    _instance_lock = threading.Lock()

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(RedisTool, "_instance"):
    #         with RedisTool._instance_lock:
    #             if not hasattr(RedisTool, "_instance"):
    #                 RedisTool._instance = object.__new__(cls)
    #                 RedisTool._instance.get_conf()
    #                 RedisTool._instance.connect()
    #     return RedisTool._instance
    #
    # def __init__(self):
    #     pass

    def get_conf(self):
        # try:
            conf = None
            conf = dict(config_file.items('redis_connection'))
            print('xxx',config_file.items('redis_connection'))
            self._host = conf['host']
            self._port = int(conf['port'])
            self._pwd = conf['pwd']
            self._db = int(conf.get('db', 0))
            self._conn = int(conf.get('conn', 5))
        # except BaseException:
        #     raise Exception('get redis config failed! redis config: %s' % conf)

    # def connect(self):
    #     pool = redis.ConnectionPool(
    #         host=self._host,
    #         port=self._port,
    #         password=self._pwd,
    #         db=self._db,
    #         max_connections=self._conn
    #     )
    #
    #     self.client = redis.StrictRedis(
    #         connection_pool=pool
    #     )
    #
    # def get_client(self):
    #     return self.client
    #
    # def get(self, key):
    #     return self.client.get(key)
    #
    # def set(self, key, value, ex=None, nx=False):
    #     self.client.set(key, value, ex=ex, nx=nx)
    #
    # def hexpireat(self, name, when):
    #     return self.client.expireat(name, when)
    #
    # def hget(self, key, field):
    #     return self.client.hget(key, field)
    #
    # def expire_time(self, name, sec):
    #     self.client.expire(name, sec)
    #
    # def hkeys(self, key):
    #     return self.client.hkeys(key)
    #
    # def hset(self, key, field, value):
    #     self.client.hset(key, field, value)
    #
    # def hmget(self, name, keys, *args):
    #     return self.client.hmget(name, keys, *args)
    #
    # def hgetall(self, key):
    #     return self.client.hgetall(key)
    #
    # def hdel(self, name, key):
    #     return self.client.hdel(name, key)
    #
    # def hmset(self, key, dict_):
    #     self.client.hmset(key, dict_)
    #
    # def getscan(self, num, match):
    #     self.client.scan(num, match)
    #
    # def get_exit(self, key):
    #     return self.client.exists(key)
    #
    # def exists(self, key):
    #     return self.client.exists(key)
    #
    # def set_rpush(self, name, value):
    #     self.client.rpush(name, value)
    #
    # def get_list(self, name):
    #     return self.client.lrange(name, 0, -1)
    #
    # def get_exit_hash(self, key, field_name):
    #     return self.client.hexists(key, field_name)
    #
    # def batch_hincr(self, key, field_count_map):
    #     p = self.client.pipeline()
    #     for field, count in field_count_map.items():
    #         p.hincrby(key, field, count)
    #
    #     return p.execute()
    #
    # def expire_timestamp(self, key, timestamp):
    #     return self.client.expireat(key, timestamp)
    #
    # def zerm(self, name, values):
    #     return self.client.zrem(name, values)
    #
    # def zrank(self, name, value):
    #     return self.client.zrank(name, value)
    #
    # def zadd(self, name, score, meb):
    #     self.client.zadd(name, score, meb)
    #
    # def zrangewithscore(self, name, start, end):
    #     return self.client.zrange(name, start, end, withscores=True)
    #
    # def zrange(self, name, start, end):
    #     return self.client.zrange(name, start, end)
    #
    # def zscore(self, name, member):
    #     return self.client.zscore(name, member)
    #
    # def zrangebyscore(self, name, min, max):
    #     return self.client.zrangebyscore(name, min, max)
    #
    # def lpush(self, key, *values):
    #     return self.client.lpush(key, *values)
    #
    # def delete(self, key):
    #     return self.client.delete(key)


if __name__ == '__main__':
    r1 = RedisTool()
    r1.get_conf()

    # print(r1.client.delete("clickhouse_info"))
