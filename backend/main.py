from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

# Import LangGraph workflow (to be implemented below)
from fastapi import FastAPI
from workflow import analyze_tourism_workflow

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing; allows all origins. Change to ["http://localhost:5173"] for production.
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple hello endpoint for frontend connection test
@app.get("/hello")
def hello():
    return {"message": "Hello World!"}

# Events endpoint returns a list of tourism-related events
@app.get("/events")
def get_events():
    return [
        {"year": 2020, "event": "Tourism Visa Launched"},
        {"year": 2021, "event": "COVID Shutdown"},
        {"year": 2022, "event": "NEOM Announced"},
        {"year": 2023, "event": "AlUla Expo"},
        {"year": 2024, "event": "Record Year"},
        {"year": 2025, "event": "Vision 2030 Prep"},
    ]

@app.get("/analyze_tourism")
def analyze_tourism():
    result = analyze_tourism_workflow()
    return JSONResponse(content=result)