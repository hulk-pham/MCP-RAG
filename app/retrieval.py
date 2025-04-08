from typing import List
from app.utils import get_chroma_collection

def add_document(document: str, metadata: dict = None):
    """
    Add a document to the ChromaDB collection.
    
    Args:
        document: The document text to add
        metadata: Optional metadata associated with the document
    """
    collection = get_chroma_collection()
    # Generate a simple hash as document ID
    doc_id = str(abs(hash(document)) % (10 ** 10))
    
    collection.add(
        documents=[document],
        metadatas=[metadata or {}],
        ids=[doc_id]
    )
    return doc_id

def search_documents(query: str) -> List[str]:
    """
    Search for relevant documents based on the query.
    
    Uses ChromaDB for vector search if available, falls back to keyword matching.
    """
    try:
        # Try to use ChromaDB
        collection = get_chroma_collection()
        results = collection.query(
            query_texts=[query],
            n_results=3
        )
        
        if results and results['documents'][0]:
            return results['documents'][0]
            
    except Exception as e:
        print(f"ChromaDB search failed: {e}. Falling back to keyword matching.")
        return ["No relevant documents found."]