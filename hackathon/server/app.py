import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import requests
from config import Config  # Import from config.py

# FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Adjust allowed origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and Response Models
class ChatRequest(BaseModel):
    user_message: str
    tweaks: Optional[dict] = {}
    output_type: Optional[str] = "chat"
    input_type: Optional[str] = "chat"

class ChatResponse(BaseModel):
    session_id: str
    response_message: str
    sender: str

# Helper Function to Call LangFlow API
def call_langflow_api(message: str, endpoint: str, tweaks: dict, output_type: str, input_type: str):
    api_url = f"{Config.BASE_API_URL}/lf/{Config.LANGFLOW_ID}/api/v1/run/{endpoint}"
    headers = {
        "Authorization": f"Bearer {Config.APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
        "tweaks": tweaks
    }
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"LangFlow API Error: {response.text}")
    return response.json()

# Function to Simplify API Response
def simplify_response(api_response):
    try:
        outputs = api_response.get("outputs", [])
        if not outputs:
            raise ValueError("No outputs in the response.")

        message_data = outputs[0].get("outputs", [])[0].get("results", {}).get("message", {})
        if not message_data:
            raise ValueError("No message found in the response.")

        return {
            "session_id": api_response.get("session_id", ""),
            "response_message": message_data.get("text", "No response text available."),
            "sender": message_data.get("sender_name", "AI")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing response: {str(e)}")

# FastAPI Endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Call LangFlow API
        raw_response = call_langflow_api(
            message=request.user_message,
            endpoint=Config.FLOW_ID,
            tweaks=request.tweaks,
            output_type=request.output_type,
            input_type=request.input_type
        )
        # Simplify and return the response
        simplified_response = simplify_response(raw_response)
        return simplified_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
