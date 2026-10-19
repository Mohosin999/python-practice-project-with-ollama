"""
Ollama Chat - Step 2
A simple, reusable chat function with error handling.
"""

import ollama

MODEL_NAME = "qwen2.5:0.5b"


def ask_ollama(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Send a single prompt to Ollama and return the text response.

    Args:
        prompt: The user's message.
        model:  Which Ollama model to use.

    Returns:
        The model's reply as plain text.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]
    except ConnectionError:
        return "ConnectionError: Unable to connect to Ollama. Please check your internet connection and try again."
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    """Entry point when the script is run directly."""
    print(f"🤖 Chatting with {MODEL_NAME} (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        reply = ask_ollama(user_input)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()
