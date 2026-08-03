from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.services.gemini_service import gemini_service
from app.services.search_service import search_service
from app.services.google_service import google_service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal AI Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    history: Optional[List[dict]] = None

class SearchRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = await gemini_service.generate_response(request.prompt, request.history)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search(request: SearchRequest):
    try:
        results = await search_service.search(request.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/auth/url")
async def get_auth_url():
    return {"url": google_service.get_auth_url()}

from app.services.task_service import task_service

class TaskRequest(BaseModel):
    title: str
    description: str
    due_date: str

@app.post("/tasks")
async def add_task(request: TaskRequest):
    return task_service.add_task(request.title, request.description, request.due_date)

@app.get("/tasks")
async def get_tasks():
    return task_service.get_tasks()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
