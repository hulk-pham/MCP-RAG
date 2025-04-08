from typing import Dict, Any

def get_user_context(user_id: str) -> Dict[str, Any]:
    """
    Retrieve user-specific context information.
    
    In a real implementation, this would query a database.
    For now, we return mock data.
    """
    # Mock user data
    user_data = {
        "user123": {
            "name": "Alice Smith",
            "role": "Product Manager",
            "department": "Product",
            "preferences": {
                "communication_style": "concise",
                "technical_level": "medium"
            },
            "recent_projects": ["Mobile App Redesign", "Customer Survey Analysis"]
        },
        "user456": {
            "name": "Bob Johnson",
            "role": "Software Engineer",
            "department": "Engineering",
            "preferences": {
                "communication_style": "detailed",
                "technical_level": "high"
            },
            "recent_projects": ["API Gateway Implementation", "Database Migration"]
        }
    }
    
    # Return user data if found, otherwise return a default profile
    return user_data.get(user_id, {
        "name": "Unknown User",
        "role": "Guest",
        "department": "N/A",
        "preferences": {
            "communication_style": "balanced",
            "technical_level": "medium"
        },
        "recent_projects": []
    }) 