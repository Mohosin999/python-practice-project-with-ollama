"""
LLM layer: all Ollama communication lives here.
Nothing else in the app should import `ollama` directly.
"""

import ollama

from src.config import MODEL_NAME


def ask(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Send a single prompt to Ollama and return the text reply.

    Raises:
        ConnectionError: if Ollama server is unreachable.
        ollama.ResponseError: if Ollama returns an error.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]
    except ConnectionError as e:
        raise ConnectionError(
            "Ollama server unreachable. Is it running? (ollama serve)"
        ) from e
