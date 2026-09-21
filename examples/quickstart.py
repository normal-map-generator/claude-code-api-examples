"""Minimal Claude API request with a system prompt.

Setup:
  pip install anthropic
  export ANTHROPIC_API_KEY=...   # never hard-code the key
  export CLAUDE_MODEL=...        # a current model id from the API reference
"""
import os

import anthropic

# The default model id here is illustrative; check the API reference for current ids.
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")

# The client reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()

response = client.messages.create(
    model=MODEL,
    max_tokens=512,  # illustrative limit; raise for longer answers
    system="You are a concise assistant. Answer in three sentences or fewer.",
    messages=[
        {"role": "user", "content": "Explain what a system prompt is for."},
    ],
)

# Print every text block in the reply.
for block in response.content:
    if block.type == "text":
        print(block.text)
