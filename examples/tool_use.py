"""One complete tool-use round trip with the Claude API.

The tool is a fake weather lookup so the loop is easy to follow:
  1. send the question plus the tool definition
  2. the model asks to call the tool
  3. run the local function and send the result back
  4. print the final answer

Setup:
  pip install anthropic
  export ANTHROPIC_API_KEY=...
  export CLAUDE_MODEL=...   # a current model id from the API reference
"""
import json
import os

import anthropic

MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")  # illustrative default
client = anthropic.Anthropic()

TOOLS = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city. Returns a short JSON object.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name"}},
            "required": ["city"],
        },
    }
]


def get_weather(city: str) -> dict:
    # Illustrative stand-in for a real API call.
    return {"city": city, "condition": "cloudy", "temperature_c": 18}


messages = [{"role": "user", "content": "What is the weather like in Lisbon right now?"}]

first = client.messages.create(model=MODEL, max_tokens=512, tools=TOOLS, messages=messages)

if first.stop_reason != "tool_use":
    print("Model answered without using the tool:")
    print("".join(b.text for b in first.content if b.type == "text"))
    raise SystemExit(0)

# Run every tool call the model requested and collect the results.
results = []
for block in first.content:
    if block.type == "tool_use" and block.name == "get_weather":
        output = get_weather(**block.input)
        results.append(
            {"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(output)}
        )

messages.append({"role": "assistant", "content": first.content})
messages.append({"role": "user", "content": results})

final = client.messages.create(model=MODEL, max_tokens=512, tools=TOOLS, messages=messages)
print("".join(b.text for b in final.content if b.type == "text"))
