# server.py
from pydantic import BaseModel
from typing import List, Optional

from app.context import get_user_context
from app.retrieval import search_documents
from app.prompt_builder import build_prompt
from app.llm_client import query_llm

# Keep the existing MCP setup
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

class QueryResponse(BaseModel):
    response: str
    documents_used: List[str]

@mcp.tool()
def process_query(user_id: str, query: str) -> QueryResponse:
    """
    Process a user query by retrieving relevant documents and generating a response
    
    Args:
        user_id: The ID of the user making the query
        query: The user's question or request
        
    Returns:
        A response object containing the answer and documents used
    """
    try:
        # Get user context
        user_context = get_user_context(user_id)
        
        # Retrieve relevant documents
        documents = search_documents(query)
        
        # Build prompt
        prompt = build_prompt(user_context, documents, query)
        
        # Query LLM
        response = query_llm(prompt)
        
        return QueryResponse(
            response=response,
            documents_used=[doc[:100] + "..." if len(doc) > 100 else doc for doc in documents]
        )
    except Exception as e:
        raise ValueError(str(e))