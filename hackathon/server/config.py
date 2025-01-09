import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Config:
    BASE_API_URL = os.getenv("BASE_API_URL")
    LANGFLOW_ID = os.getenv("LANGFLOW_ID")
    APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
    FLOW_ID = os.getenv("FLOW_ID")
