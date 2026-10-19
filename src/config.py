"""
Application configuration.
Reads from environment variables with sensible defaults.
"""

import os

# Model settings
MODEL_NAME: str = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")
OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# Behavior
EXIT_COMMANDS: set[str] = {"quit", "exit", "q"}