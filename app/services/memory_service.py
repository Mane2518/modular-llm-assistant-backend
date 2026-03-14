import redis
import json
from app.core.config import settings

class MemoryService:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )

    def add_message(self, session_id: str, role: str, content: str):
        message = {"role": role, "content": content}
        self.redis_client.rpush(f"history:{session_id}", json.dumps(message))

    def get_history(self, session_id: str):
        messages = self.redis_client.lrange(f"history:{session_id}", 0, -1)
        return [json.loads(m) for m in messages]

    def clear_history(self, session_id: str):
        self.redis_client.delete(f"history:{session_id}")
