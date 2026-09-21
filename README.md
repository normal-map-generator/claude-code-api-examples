# Claude Code API examples

*Unofficial community examples for Claude Code and the Claude API. Not affiliated with Anthropic. All trademarks belong to their owners.*

Three short Python scripts for anyone who searched claude code api and wants to make a first request to the Claude API rather than read another overview. They follow the order the API course teaches: a basic request with a system prompt, then streaming, then a single tool-use round trip. The API key is read from the environment in every file. Model ids change over time, so each script takes the model from `CLAUDE_MODEL` and treats the default as illustrative; pick a current id from the API reference.

> Want an app rather than an API client? [Try Begin.sh - prompt or URL in, static site or Expo app zip out](https://begin.sh?utm_source=github&utm_medium=ugc&utm_campaign=claude-code-api-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
|---|---|
| `examples/quickstart.py` | One request with a system prompt; prints the text reply. |
| `examples/streaming.py` | The same request streamed token by token. |
| `examples/tool_use.py` | Defining one tool, handling the tool call, returning the result. |

## Setup

```
pip install anthropic
export ANTHROPIC_API_KEY=your-key-from-the-console
export CLAUDE_MODEL=claude-sonnet-5   # illustrative; use a current id from the API reference
```

Create the key in the [Claude Console](https://platform.claude.com/). The [quickstart](https://platform.claude.com/docs/en/get-started) and [API reference](https://platform.claude.com/docs/en/api/overview) are the authority for parameter names and current models; the scripts use the minimal, long-stable shape (a model, a token limit, a system prompt and a list of messages).

## examples/quickstart.py

Creates a client, sends a single user message with a short system prompt, and prints the text of the reply. This is the 'authentication, basic requests, system prompts' part of the course's first section in about twenty lines. Change the prompt and run it again; nothing else needs to change.

## examples/streaming.py

Same request, but the response is consumed as a stream and printed as it arrives. Use this shape for anything user-facing; waiting for a full response feels slow even when it is not.

## examples/tool_use.py

Declares one tool (a fake weather lookup with a JSON schema for its input), sends a question that needs it, and handles the round trip: the model asks to call the tool, the script runs a local function, sends the result back, and prints the final answer. The tool is deliberately trivial so the loop is visible. The course covers multi-turn and batch tool calling beyond this; this is the smallest complete case.

## When to use Begin.sh instead

If the reason you are reading API examples is that you need a landing page, a docs site or a small Expo app, you do not need an API client at all. [Try Begin.sh - a prompt or a URL to clone becomes a working static site or Expo app you download as a zip](https://begin.sh?utm_source=github&utm_medium=ugc&utm_campaign=claude-code-api-examples&utm_content=readme-top&utm_term=tier-r). No hosting, backend or auth; you keep the files.
