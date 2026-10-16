# Agentic IT Incident Assistant

An AI-assisted IT incident investigation project built using Python, LangGraph, MCP, and FastAPI.

## Features

- Application health monitoring
- Error log analysis
- Knowledge-base lookup
- Conditional incident escalation
- LangGraph workflow orchestration
- MCP server and tools
- FastAPI backend
- Web interface

## Tech Stack

Python, Pandas, LangGraph, LangChain, MCP, FastAPI, Uvicorn, Gemini API

## Architecture

User → FastAPI → LangGraph → Monitoring Tools → Knowledge Base → Decision → Incident Escalation

## Run Locally

1. Create a virtual environment.
2. Install dependencies:

   pip install -r requirements.txt

3. Start the application:

   python -m uvicorn api:api --reload

4. Open:

   http://127.0.0.1:8000/

## Notes

- Uses mock CSV datasets for demonstration.
- Gemini integration requires a separate API key.
- Known resolutions are suggested, not automatically executed.
- Incident tickets are stored locally in CSV.