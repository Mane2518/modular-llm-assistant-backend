from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse, HistoryResponse
from app.services.llm_service import LLMService
from app.services.memory_service import MemoryService

router = APIRouter()
llm_service = LLMService()
memory_service = MemoryService()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # 1. Get history
        history = memory_service.get_history(request.session_id)
        
        # 2. Get LLM response
        response_text = await llm_service.get_response(request.message, history)
        
        # 3. Update memory
        memory_service.add_message(request.session_id, "user", request.message)
        memory_service.add_message(request.session_id, "assistant", response_text)
        
        return ChatResponse(response=response_text, session_id=request.session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memory/{session_id}", response_model=HistoryResponse)
async def get_memory(session_id: str):
    history = memory_service.get_history(session_id)
    return HistoryResponse(history=history)

@router.delete("/memory/{session_id}")
async def clear_memory(session_id: str):
    memory_service.clear_history(session_id)
    return {"message": "History cleared"}
