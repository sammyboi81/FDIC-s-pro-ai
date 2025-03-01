import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import requests

# Load environment variables
load_dotenv()

# Get API key and agent ID from environment variables or use defaults
API_KEY = os.getenv("API_KEY", "your_api_key_here")
AGENT_ID = os.getenv("AGENT_ID", "a6e20b090d83f39cc19599e0a37e7ce12f31b7255")
API_ENDPOINT = os.getenv("API_ENDPOINT", "https://api.your-service.com/agent")

# Initialize FastAPI app
app = FastAPI(title="FDt Pro AI", description="AI Agent API")

class Query(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Welcome to FDt Pro AI! Send a POST request to /query to interact with the agent."}

@app.post("/query")
async def process_query(query: Query):
    try:
        # Call the agent API with the agent ID
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "agent_id": AGENT_ID,
            "prompt": query.prompt
        }
        
        response = requests.post(
            API_ENDPOINT,
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Agent API error: {response.text}"
            )
            
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)