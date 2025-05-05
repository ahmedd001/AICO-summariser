from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.services.summarizer import fetch_web_content, summarize_web_content, extract_main_topic
from src.services.memory import conversation

app = FastAPI()

class SummarizeRequest(BaseModel):
    url: str
    question: Optional[str] = None  

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    try:
        if request.question:
            response = conversation.invoke({"input": request.question})
            return {"response": response["response"]}

        content = fetch_web_content(request.url)
        summary = summarize_web_content(content)
        topic = extract_main_topic(summary)

        intro_prompt = f"Here is a summary of the webpage at {request.url}:\n{summary}"
        conversation.invoke({"input": intro_prompt})  

        return {
            "summary": summary,
            "main_topic": topic
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/memory")
def get_memory():
    return {
        "memory": [m.content for m in conversation.memory.chat_memory.messages]
    }
    
