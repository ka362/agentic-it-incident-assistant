from fastapi import FastAPI
from pydantic import BaseModel
from graph import app
from fastapi.responses import FileResponse
from pathlib import Path

api = FastAPI(title="Agentic IT Incident Assistant")


class IncidentRequest(BaseModel):
    application_name: str


#@api.get("/")
@api.get("/")
def home():
    return FileResponse(Path(__file__).parent / "index.html")

@api.post("/investigate")
def investigate(request: IncidentRequest):
    result = app.invoke({
        "application_name": request.application_name
    })

    return result