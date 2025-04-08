import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

from app.context import add_user_context

# Sample mock data
mock_users = [
    {
        "user_id": "user_001",
        "context": {
            "name": "Alex Johnson",
            "role": "Software Engineer",
            "department": "Engineering",
            "preferences": {
                "communication_style": "direct",
                "code_examples": "python",
                "explanation_detail": "high"
            },
            "recent_projects": ["API Gateway", "Authentication Service"]
        }
    },
    {
        "user_id": "user_002",
        "context": {
            "name": "Sam Taylor",
            "role": "Product Manager",
            "department": "Product",
            "preferences": {
                "communication_style": "visual",
                "technical_detail": "low",
                "business_focus": "high"
            },
            "recent_projects": ["User Dashboard", "Analytics Platform"]
        }
    },
    {
        "user_id": "user_003",
        "context": {
            "name": "Jordan Lee",
            "role": "Data Scientist",
            "department": "Data",
            "preferences": {
                "communication_style": "analytical",
                "code_examples": "python",
                "statistical_detail": "high"
            },
            "recent_projects": ["Recommendation Engine", "Customer Segmentation"]
        }
    }
]

def migrate_mock_data():
    """Add mock user data to the database"""
    print("Starting migration of mock user data...")
    
    for user in mock_users:
        try:
            add_user_context(user["user_id"], user["context"])
            print(f"Added user: {user['context']['name']} ({user['user_id']})")
        except Exception as e:
            print(e.with_traceback())
            # print(f"Error adding user {user['user_id']}: {e}")
    
    print("Migration completed!")

if __name__ == "__main__":
    migrate_mock_data() 