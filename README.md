# Semantic Kernel Project

A comprehensive demonstration of **Microsoft's Semantic Kernel** framework for building AI-powered applications with semantic memory, skill management, and intelligent planning.

## Features

- **Semantic Memory Store**: Persistent vector database using ChromaDB with OpenAI embeddings for semantic search and retrieval
- **Skill Integration**: Demonstrates importing and chaining core skills (Math, FileIO, Time, Text)
- **Action Planning**: Uses ActionPlanner to intelligently select appropriate functions based on natural language queries
- **SWOT Analysis**: Real-world business case study storing and retrieving structured business analysis data
- **OpenAI Integration**: Leverages GPT-3.5-turbo and text-embedding-ada-002 for completions and embeddings

## Setup

1. Install Python 3.12 (recommended path on macOS with Homebrew):

```bash
brew install python@3.12
```

2. Install the compatible package versions globally (no virtual environment):

```bash
/opt/homebrew/bin/python3.12 -m pip install --upgrade pip --break-system-packages
/opt/homebrew/bin/python3.12 -m pip install semantic-kernel==0.3.15.dev0 ipython setuptools<70 --break-system-packages
/opt/homebrew/bin/python3.12 -m pip install --break-system-packages "pydantic==1.10.26" "fastapi==0.99.1" "starlette==0.27.0" "chromadb==0.4.15"
```

**Note**: ChromaDB version 0.4.15 is required (not 0.4.24) due to embedding function interface changes in chromadb 0.4.16+.

3. Add your credentials to a `.env` file in the project root.

For OpenAI:

```env
OPENAI_API_KEY=your_api_key
OPENAI_ORG_ID=your_org_id
```

For Azure OpenAI:

```env
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
```

## Project Structure

```
├── memory-store.py       # Semantic memory with SWOT analysis and similarity search
├── importing-skills.py   # ActionPlanner demo for skill selection
├── adding-skills.py      # Custom skill registration
├── app.py                # Main application entry point
├── swot.py               # SWOT analysis logic
├── mymemories/           # Persistent ChromaDB vector store
└── README.md             # This file
```

## Run

### Memory Store Demo
```bash
python3.12 memory-store.py
```
Demonstrates:
- Creating a semantic memory store with ChromaDB
- Storing SWOT analysis data with embeddings
- Semantic search using natural language queries
- Retrieving business insights based on relevance scores

### Importing Skills Demo
```bash
python3.12 importing-skills.py
```
Demonstrates:
- Importing core skills (Math, FileIO, Time, Text)
- ActionPlanner automatically selecting appropriate functions
- Natural language to function mapping

### Main App
```bash
python3.12 app.py
```
Runs the primary application entry point.

## Current App Behavior

- Uses `OpenAIChatCompletion` by default (`useAzureOpenAI = False`)
- Switch `useAzureOpenAI = True` to use Azure OpenAI
- Registers semantic functions for text summarization and analysis
- Runs async calls via `asyncio.run(main())`

## Recent Fixes (July 2026)

### memory-store.py
- ✅ Resolved ChromaDB collection conflict by clearing persistent database
- ✅ Downgraded chromadb from 0.4.24 to 0.4.15 to fix embedding function interface incompatibility
- ✅ Restored compatible baseline versions (pydantic, fastapi, starlette)

### importing-skills.py
- ✅ Fixed UnboundLocalError by separating action_planner and seq_planner into distinct variables
- ✅ Moved planner initialization outside of async main() to resolve Python scoping issues
- ✅ Disabled SequentialPlanner demo and LiterateFriend skill import (pending plugins-sk directory setup)

## Technology Stack

- **Semantic Kernel 0.3.15.dev0** - Microsoft's AI orchestration framework
- **ChromaDB 0.4.15** - Vector database for embeddings
- **Pydantic 1.10.26** - Data validation
- **OpenAI API** - GPT-3.5-turbo & text-embedding-ada-002
- **Python 3.12**

## Troubleshooting

### Collection already exists error
```bash
rm -rf mymemories/chroma.sqlite3
```

### ChromaDB embedding function error
Ensure you have chromadb==0.4.15 (not 0.4.24+) installed.

### Verify environment
```bash
/opt/homebrew/bin/python3.12 -c "import importlib.metadata as m; print('semantic-kernel', m.version('semantic-kernel')); print('chromadb', m.version('chromadb'))"
```

## Notes

- `display(Markdown(...))` renders rich output in Jupyter. In terminal runs, you may see a Markdown object representation.
- If dependencies are missing or mismatched, reinstall with the exact setup commands above.
