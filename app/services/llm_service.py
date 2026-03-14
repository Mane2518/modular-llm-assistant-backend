from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY)

    async def get_response(self, prompt: str, history: list = None):
        messages = [SystemMessage(content="You are a helpful AI assistant.")]
        
        if history:
            for msg in history:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(AIMessage(content=msg["content"]))
        
        messages.append(HumanMessage(content=prompt))
        
        response = await self.llm.agenerate([messages])
        return response.generations[0][0].text
