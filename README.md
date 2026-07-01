# Semantic Kernel Project

This project uses `semantic-kernel` with a Hugging Face text completion connector.

## Setup

1. Make sure you have Python 3.13 installed.
2. Create a virtual environment (if one is not already present):

```bash
cd /Users/dennispitadeniya/Documents/Sementic-kernal-project
python3 -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
.venv/bin/python app.py
```

If the virtual environment is activated, you can also run:

```bash
python app.py
```

## Dependencies

- semantic-kernel
- transformers
- torch

## Notes

- The project currently uses the Hugging Face connector in `app.py`.
- If you run into any missing package errors, reinstall dependencies with:

```bash
pip install -r requirements.txt
```
