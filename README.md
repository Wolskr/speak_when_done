# speak_when_done

An MCP server that allows Claude to speak notifications aloud using Kyutai's Pocket TTS.

## Purpose

This MCP server provides Claude with the ability to notify you audibly when long-running tasks complete. Instead of switching back to check on progress, Claude will speak to you when it needs your attention.

## Prerequisites

- macOS (uses `afplay` for audio playback)
- [uv](https://docs.astral.sh/uv/) package manager
- `pocket-tts` available via uvx

Test that pocket-tts works:
```bash
uvx pocket-tts generate --text "test" --quiet
```

## Installation

Add this MCP server to Claude Code:

```bash
claude mcp add speak_when_done -s user -- uv run --directory ~/localdev/speak_when_done python server.py
```

Or for project-specific configuration:

```bash
claude mcp add speak_when_done -- uv run --directory ~/localdev/speak_when_done python server.py
```

## Usage

Once installed, Claude has access to a `speak` tool. The tool is designed to be used only when Claude needs your attention after something significant completes.

### Tool: `speak`

**Parameters:**
- `message` (required): The message to speak aloud
- `voice` (optional): Voice to use (default: "alba")

**Example uses:**
- Build completion notifications
- Test suite results
- Deployment status
- When Claude finds what you asked for during a long search

## Recommended Claude Instructions

Add to your Claude Code custom instructions or CLAUDE.md:

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

**MCP not connecting:**
Check the MCP server status:
```bash
claude mcp list
claude mcp get speak_when_done
```
