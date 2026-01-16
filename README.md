# speak_when_done

Text-to-speech with automatic temp file handling. Speaks text aloud and cleans up after itself.

Works as a CLI tool, Python library, or MCP server for AI assistants.

## What it does

```bash
uvx speak_when_done --text "Your build is complete"
```

That's it. It generates speech, plays it, and cleans up the temp file automatically.

### As an MCP server

You kick off a long task (build, test suite, deployment) and go do something else. When it's done, your AI speaks to you:

> "Your build completed successfully with no errors."

> "The test suite finished. 47 passed, 2 failed."

> "I found the bug you were looking for in the auth module."

## Prerequisites

- macOS (uses `afplay` for audio playback)
- [uv](https://docs.astral.sh/uv/) package manager

Test that pocket-tts works:
```bash
uvx pocket-tts generate --text "hello world" --quiet
```

## Installation

### CLI (via uvx)

No installation needed! Just run:
```bash
uvx speak_when_done --text "Hello world"
```

Options:
```bash
uvx speak_when_done --text "Hello" --voice alba    # specify voice
uvx speak_when_done --text "Hello" --quiet         # suppress TTS output
uvx speak_when_done -t "Hello" -v alba -q          # short flags
```

### Python library

```bash
pip install speak-when-done
# or
uv add speak-when-done
```

```python
from speak_when_done import speak

result = speak("Hello world")
result = speak("Hello", voice="alba", quiet=True)
```

### MCP Server for Claude Code

Add globally (available in all projects):
```bash
claude mcp add speak_when_done -s user -- uv run --directory /path/to/speak_when_done python -m speak_when_done.server
```

Or project-specific:
```bash
claude mcp add speak_when_done -- uv run --directory /path/to/speak_when_done python -m speak_when_done.server
```

### MCP Server for Cursor

Add to `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project):

```json
{
  "mcpServers": {
    "speak_when_done": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/speak_when_done",
        "python",
        "-m",
        "speak_when_done.server"
      ]
    }
  }
}
```

Then restart Cursor or reload the window.

## Usage with AI assistants

Once installed as an MCP server, your AI has access to a `speak` tool. Ask it to notify you when something finishes:

> "Run the full test suite and tell me out loud when it's done"

> "Deploy to staging and speak to me when it completes"

> "Search for all usages of the deprecated API and let me know what you find"

## Recommended Instructions

Add to your custom instructions or CLAUDE.md:

```
When using the speak_when_done MCP:
- Only use the speak tool after completing long-running tasks (builds, tests, deployments, extensive searches)
- Keep spoken messages brief and informative
- Do not use speak for routine responses or simple questions
```

## Voices

Pocket TTS supports multiple voices. The default "alba" is a natural-sounding voice. You can also provide a path to an audio file for voice cloning.

## Troubleshooting

**"Command not found" error:**
Make sure `uvx` and `pocket-tts` are available in your PATH.

**No audio playback:**
Ensure your macOS audio is not muted and `afplay` is working:
```bash
afplay /System/Library/Sounds/Glass.aiff
```

**MCP not connecting in Claude Code:**
```bash
claude mcp list
claude mcp get speak_when_done
```

**MCP not connecting in Cursor:**
Check Settings → Features → MCP to ensure MCP is enabled, then verify your JSON config is valid.
