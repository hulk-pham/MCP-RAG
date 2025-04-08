import os
import json
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from app.utils import get_chroma_client, getenv
load_dotenv()

client = get_chroma_client()
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small"
)

# Get or create collection
def get_collection():
    try:
        connection = client.get_or_create_collection(
            name="user_contexts", 
            embedding_function=openai_ef
        )

        return connection
    except ValueError:
        print("Failed to get or create collection")
        raise ValueError("Failed to get or create collection")

def context_to_text(context_dict: Dict[str, Any]) -> str:
    """Convert user context dictionary to a single text string for embedding"""
    text_parts = [
        f"Name: {context_dict.get('name', 'Unknown')}",
        f"Role: {context_dict.get('role', 'Unknown')}",
        f"Department: {context_dict.get('department', 'Unknown')}"
    ]
    
    # Add preferences
    prefs = context_dict.get('preferences', {})
    for k, v in prefs.items():
        text_parts.append(f"Preference {k}: {v}")
    
    # Add projects
    projects = context_dict.get('recent_projects', [])
    if projects:
        text_parts.append(f"Recent projects: {', '.join(projects)}")
    
    return " ".join(text_parts)

def add_user_context(user_id: str, context_dict: Dict[str, Any]) -> None:
    """
    Add or update a user context in ChromaDB
    
    Args:
        user_id: Unique identifier for the user
        context_dict: Dictionary containing user context information
    """
    collection = get_collection()

    # Convert context to text for embedding
    context_text = context_to_text(context_dict)
    
    # Create metadata
    metadata = {
        "role": context_dict.get("role", "Unknown"),
        "department": context_dict.get("department", "Unknown"),
        "full_context": json.dumps(context_dict)  # Store full context as JSON
    }
    
    # Add or update document
    try:
        collection.upsert(
            ids=[user_id],
            documents=[context_text],
            metadatas=[metadata]
        )
    except Exception as e:
        print(f"Error adding user context: {e}")
        raise

def get_user_context(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve user context by exact ID
    
    Args:
        user_id: Unique identifier for the user
        
    Returns:
        User context dictionary or None if not found
    """
    collection = get_collection()
    
    try:
        result = collection.get(ids=[user_id], include=["metadatas"])
        
        if result and result["metadatas"]:
            # Extract the full context from metadata
            return json.loads(result["metadatas"][0]["full_context"])
        return None
    except Exception as e:
        print(f"Error retrieving user context: {e}")
        return None

def search_user_context(query: str, top_k: int = 1) -> List[Dict[str, Any]]:
    """
    Search for user contexts semantically similar to the query
    
    Args:
        query: Search query
        top_k: Number of results to return
        
    Returns:
        List of user context dictionaries
    """
    collection = get_collection()
    
    try:
        results = collection.query(
            query_texts=[query],
            n_results=top_k,
            include=["metadatas", "documents", "distances"]
        )
        
        contexts = []
        if results and results["metadatas"]:
            for metadata in results["metadatas"][0]:
                contexts.append(json.loads(metadata["full_context"]))
        
        return contexts
    except Exception as e:
        print(f"Error searching user contexts: {e}")
        return [] 