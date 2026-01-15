"""
MCP Server for text-to-speech notifications.

Uses Kyutai's Pocket TTS to speak notifications to the user when Claude
needs their attention after long-running tasks complete.
"""

import logging
import subprocess
import sys
import tempfile
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Configure logging to stderr (never stdout - it corrupts JSON-RPC)
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create the MCP server
mcp = FastMCP("speak_when_done")


@mcp.tool()
def speak(message: str, voice: str = "alba") -> dict:
    """
    Speak a message aloud to notify the user.

    Use this tool ONLY when you need to get the user's attention after
    a long-running task has completed. Do not use for routine responses.

    Good examples:
    - "Your build has completed successfully"
    - "The test suite finished with 3 failures"
    - "Deployment is complete"
    - "I found the bug you were looking for"

    Args:
        message: The message to speak aloud. Keep it brief and informative.
        voice: Voice to use for speech (default: alba). Can be a built-in
               voice name or path to an audio file for voice cloning.

    Returns:
        Dictionary with success status and details.
    """
    try:
        logger.info(f"Speaking message: {message[:50]}...")

        # Create a temp file for the output audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            output_path = tmp.name

        # Call pocket-tts via uvx
        cmd = [
            "uvx", "pocket-tts", "generate",
            "--text", message,
            "--voice", voice,
            "--output-path", output_path,
            "--quiet",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0:
            logger.error(f"pocket-tts failed: {result.stderr}")
            return {
                "success": False,
                "error": f"TTS generation failed: {result.stderr}",
            }

        # Play the audio file using macOS afplay
        play_result = subprocess.run(
            ["afplay", output_path],
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Clean up the temp file
        try:
            os.unlink(output_path)
        except OSError:
            pass

        if play_result.returncode != 0:
            logger.error(f"afplay failed: {play_result.stderr}")
            return {
                "success": False,
                "error": f"Audio playback failed: {play_result.stderr}",
            }

        logger.info("Message spoken successfully")
        return {
            "success": True,
            "message": "Notification spoken to user",
            "spoken_text": message,
        }

    except subprocess.TimeoutExpired:
        logger.error("TTS operation timed out")
        return {
            "success": False,
            "error": "Operation timed out",
        }
    except FileNotFoundError as e:
        logger.error(f"Command not found: {e}")
        return {
            "success": False,
            "error": f"Required command not found: {e}",
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return {
            "success": False,
            "error": str(e),
        }


if __name__ == "__main__":
    logger.info("Starting speak_when_done MCP server")
    mcp.run()
