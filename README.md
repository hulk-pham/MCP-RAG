# RAG Application
A demo of Retrieval-Augmented Generation (RAG) application with MCP server integration.

![Screenshot](./github/screenshot.png)

## Features
- MCP server integration
- Document retrieval using vector search with ChromaDB
- Context-aware prompt generation
- Integration with LLM APIs

## Installation
```
pip install -r requirements.txt
```

## Usage
Connect to the MCP server with Claude Desktop, Cursor, or your preferred IDE.

Use the `process_query` tool to ask questions about the company.

## Configuration
Set up your environment variables in .env:
```
OPENAI_API_KEY=your_api_key
```

## Project Structure
app/retrieval.py: Document retrieval functionality
app/context.py: Context management
app/llm_client.py: LLM API integration
app/prompt_builder.py: Prompt construction

## License
MIT