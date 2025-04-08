from typing import List

def search_documents(query: str) -> List[str]:
    """
    Search for relevant documents based on the query.
    
    In a real implementation, this would use vector search (e.g., ChromaDB).
    For now, we return mock documents based on simple keyword matching.
    """
    # Mock document database
    documents = [
        "Our company's vacation policy allows for 20 days of paid time off per year. Employees must request time off at least 2 weeks in advance.",
        "The quarterly financial report shows a 15% increase in revenue compared to the previous quarter. Major growth areas include enterprise sales and the new mobile product line.",
        "The engineering team uses a Git workflow where features are developed in branches and merged via pull requests. Code reviews are required before merging.",
        "Our product roadmap for Q3 includes launching the mobile app redesign, implementing single sign-on, and improving analytics dashboard performance.",
        "The company security policy requires all employees to use two-factor authentication and change passwords every 90 days.",
        "Customer satisfaction surveys indicate that users find our new interface intuitive but would like more customization options."
    ]
    
    # Simple keyword matching (in a real system, use vector similarity)
    relevant_docs = []
    query_terms = query.lower().split()
    
    for doc in documents:
        doc_lower = doc.lower()
        if any(term in doc_lower for term in query_terms):
            relevant_docs.append(doc)
    
    # Return top 3 documents or all if fewer than 3
    return relevant_docs[:3] if relevant_docs else ["No relevant documents found."] 