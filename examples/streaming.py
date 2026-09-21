"""Stream a Claude API response and print it as it arrives.

Setup:
  pip install anthropic
  export ANTHROPIC_API_KEY=...
  export CLAUDE_MODEL=...   # a current model id from the API reference
"""
import os
import sys

import anthropic

MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")  # illustrative default

client = anthropic.Anthropic()  # key from ANTHROPIC_API_KEY

prompt = " ".join(sys.argv[1:]) or "Write a short paragraph about why streaming matters in a chat UI."

with client.messages.stream(
    model=MODEL,
    max_tokens=512,  # illustrative
    messages=[{"role": "user", "content": prompt}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print()
