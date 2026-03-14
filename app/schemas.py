from pydantic import BaseModel
from typing import List, Dict

class ChatRequest(BaseModel):
    message: str
    session_id: str

class ChatResponse(BaseModel):
    response: str
    session_id: str

class HistoryResponse(BaseModel):
    history: List[Dict[str, str]]
