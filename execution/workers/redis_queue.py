import json

import redis


class RedisQueue:

    def __init__(
        self,
        host="localhost",
        port=6379,
    ):
        self.redis = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,
        )

    def push(
        self,
        queue,
        payload,
    ):
        self.redis.rpush(
            queue,
            json.dumps(payload),
        )

    def pop(self, queue):

        result = self.redis.lpop(queue)

        if not result:
            return None

        return json.loads(result)
