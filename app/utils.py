import os
from typing import Optional
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

def getenv(key: str, default: Optional[str] = None) -> str:
    """Get environment variable with optional default value."""
    return os.getenv(key, default)

def get_chroma_client():
    """Get or create a ChromaDB client."""
    persist_dir = getenv("CHROMA_PERSIST_DIR", "./chroma_db")
    return chromadb.Client(Settings(persist_directory=persist_dir))

def get_chroma_collection(name: str = "documents"):
    """Get or create a ChromaDB collection by name."""
    client = get_chroma_client()
    return client.get_or_create_collection(name) 