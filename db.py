import os
from pathlib import Path
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(Path(__file__).parent / ".env")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "afuopulse")
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY", "")
JWT_SECRET = os.environ.get("JWT_SECRET", "dev-secret-change-me")
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
APP_ENV = os.environ.get("APP_ENV", "development")
