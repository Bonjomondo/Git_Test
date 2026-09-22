#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A minimal command-line AI agent using the OpenAI Responses API.

Setup:
    pip install -r requirements.txt
    cp .env.example .env
    # Put your API key in .env
    python agent.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI


SYSTEM_PROMPT = """
You are a small command-line coding assistant.
Answer clearly and concisely.
When the user asks about code, explain the key idea first and then give an example.
""".strip()


def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and add your API key."
        )

    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    client = OpenAI(api_key=api_key)

    print(f"Simple Agent started (model: {model})")
    print("Type 'exit' or 'quit' to stop.\n")

    previous_response_id = None

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Agent > Bye!")
            break

        if not user_input:
            continue

        request = {
            "model": model,
            "instructions": SYSTEM_PROMPT,
            "input": user_input,
        }

        # Reuse the previous response so the agent can continue the conversation.
        if previous_response_id:
            request["previous_response_id"] = previous_response_id

        try:
            response = client.responses.create(**request)
        except Exception as exc:
            print(f"Agent > API request failed: {exc}\n")
            continue

        print(f"Agent > {response.output_text}\n")
        previous_response_id = response.id


if __name__ == "__main__":
    main()
