from typing import Dict, Any, List

def build_prompt(user_context: Dict[str, Any], documents: List[str], query: str) -> str:
    """
    Build a prompt for the LLM by combining user context, retrieved documents, and the query.
    """
    # Format user context
    user_info = f"""
USER CONTEXT:
Name: {user_context.get('name', 'Unknown')}
Role: {user_context.get('role', 'Unknown')}
Department: {user_context.get('department', 'Unknown')}
Communication preference: {user_context.get('preferences', {}).get('communication_style', 'balanced')}
Technical level: {user_context.get('preferences', {}).get('technical_level', 'medium')}
Recent projects: {', '.join(user_context.get('recent_projects', ['None']))}
"""

    # Format retrieved documents
    docs_info = "RELEVANT INFORMATION:\n"
    for i, doc in enumerate(documents, 1):
        docs_info += f"{i}. {doc}\n\n"
    
    # Build the final prompt
    prompt = f"""You are an internal company assistant. Answer the following query based on the user's context and the relevant information provided.

{user_info}

{docs_info}

USER QUERY: {query}

Please provide a helpful, accurate response tailored to the user's role and preferences.
"""
    
    return prompt 