"""
CLI layer: user-facing terminal loop.
"""

from src.config import EXIT_COMMANDS, MODEL_NAME
from src.llm import ask


def main() -> None:
    print(f"🤖 Chatting with {MODEL_NAME} (type 'quit' to exit)\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Bye!")
            return

        if not user_input:
            continue

        if user_input.lower() in EXIT_COMMANDS:
            print("👋 Bye!")
            return

        try:
            reply = ask(user_input)
            print(f"Bot: {reply}\n")
        except Exception as e:
            print(f"❌ {e}\n")
