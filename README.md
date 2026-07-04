# Semantic Kernel Project

This project uses Semantic Kernel with OpenAI (or Azure OpenAI) chat completion to summarize text.

## Setup

1. Install Python 3.12 (recommended path on macOS with Homebrew):

```bash
brew install python@3.12
```

2. Install the compatible package versions globally (no virtual environment):

```bash
/opt/homebrew/bin/python3.12 -m pip install --upgrade pip --break-system-packages
/opt/homebrew/bin/python3.12 -m pip install semantic-kernel==0.3.15.dev0 ipython setuptools<70 --break-system-packages
```

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

## Run

```bash
cd /Users/dennispitadeniya/Documents/GitHub/Semantic-kernel-project
/opt/homebrew/bin/python3.12 app.py
```

## Current App Behavior

- Uses `OpenAIChatCompletion` by default (`useAzureOpenAI = False`).
- Switch `useAzureOpenAI = True` to use Azure OpenAI.
- Registers a semantic function that summarizes input to under 140 characters.
- Runs the async call via `asyncio.run(main())`.

## Notes

- `display(Markdown(...))` renders rich output in Jupyter. In terminal runs, you may see a Markdown object representation.
- If dependencies are missing or mismatched, reinstall with the exact setup commands above.
