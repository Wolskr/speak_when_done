"""
speak_when_done - Text-to-speech with automatic temp file handling.

Generates speech using Kyutai's Pocket TTS, plays it, and cleans up.
"""

import os
import subprocess
import tempfile

__version__ = "0.1.0"

# Built-in voices available in Pocket TTS
BUILTIN_VOICES = [
    {"name": "alba", "description": "Default female voice"},
    {"name": "alicia", "description": "Female voice variant"},
    {"name": "carla", "description": "Female voice variant"},
    {"name": "charlie", "description": "Male voice"},
    {"name": "danna", "description": "Female voice variant"},
    {"name": "elena", "description": "Female voice variant"},
    {"name": "emily", "description": "Female voice variant"},
    {"name": "erica", "description": "Female voice variant"},
    {"name": "guy", "description": "Male voice"},
    {"name": "jessica", "description": "Female voice variant"},
    {"name": "ken", "description": "Male voice variant"},
    {"name": "laura", "description": "Female voice variant"},
    {"name": "lina", "description": "Female voice variant"},
    {"name": "luca", "description": "Male voice variant"},
    {"name": "lucia", "description": "Female voice variant"},
    {"name": "mark", "description": "Male voice"},
    {"name": "maya", "description": "Female voice variant"},
    {"name": "michael", "description": "Male voice"},
    {"name": "mira", "description": "Female voice variant"},
    {"name": "nisha", "description": "Female voice variant"},
    {"name": "paola", "description": "Female voice variant"},
    {"name": "rosie", "description": "Female voice variant"},
    {"name": "sandra", "description": "Female voice variant"},
    {"name": "sara", "description": "Female voice variant"},
    {"name": "sarah", "description": "Female voice variant"},
    {"name": "sophia", "description": "Female voice variant"},
    {"name": "tom", "description": "Male voice"},
]


def list_voices() -> dict:
    """
    List available voices for text-to-speech.

    Returns:
        Dictionary with list of built-in voices and instructions for custom voices.
    """
    return {
        "success": True,
        "builtin_voices": BUILTIN_VOICES,
        "default_voice": "alba",
        "custom_voice_hint": "You can also use a path to an audio file for voice cloning.",
    }


def speak(message: str, voice: str = "alba", quiet: bool = False) -> dict:
    """
    Speak a message aloud using Pocket TTS.

    Handles temp file creation and cleanup automatically.

    Args:
        message: The message to speak aloud.
        voice: Voice to use (default: "alba"). Can be a built-in voice name
               or path to an audio file for voice cloning.
        quiet: If True, suppress pocket-tts output.

    Returns:
        Dictionary with success status and details.
    """
    output_path = None
    try:
        # Create a temp file for the output audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            output_path = tmp.name

        # Call pocket-tts via uvx
        cmd = [
            "uvx", "pocket-tts", "generate",
            "--text", message,
            "--voice", voice,
            "--output-path", output_path,
        ]
        if quiet:
            cmd.append("--quiet")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0:
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

        if play_result.returncode != 0:
            return {
                "success": False,
                "error": f"Audio playback failed: {play_result.stderr}",
            }

        return {
            "success": True,
            "message": "Notification spoken to user",
            "spoken_text": message,
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Operation timed out",
        }
    except FileNotFoundError as e:
        return {
            "success": False,
            "error": f"Required command not found: {e}",
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }
    finally:
        # Always clean up the temp file
        if output_path:
            try:
                os.unlink(output_path)
            except OSError:
                pass
