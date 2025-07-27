# ChatGPT Powered Terminal Command Generator

A lightweight command-line tool that uses AI to generate shell commands from natural language requests.

Example usages:

Show command and ask for confirmation before executing:
```bash
ai "find python files"
# Output: Generated command: find . -name "*.py"
# Execute this command? (y/N):
```

Just display the generated command without executing:
```bash
ai "show current date" -d
# Output: date
```

Automatically run the generated command without confirmation:
```bash
ai "show current date" -e
```

## Installation

### Quick Install (Recommended)

```bash
pip install git+https://github.com/dan2labs/term-ai.git
```

### Manual Install

1. Clone the repository:
```bash
git clone https://github.com/dan2labs/term-ai.git
cd term-ai
```

2. Install the package:
```bash
pip install .
```

## Setup

1. Add the API key to the `.env` file in your home directory:
```bash
echo "TERMAI_OPENAI_API_KEY=your_openai_api_key_here" >> ~/.env
```

2. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

Simply use the `ai` command followed by your request:

```bash
# Find files
ai "find all python files in current directory"

# Check disk usage
ai "show me disk usage for this folder"

# Search for content
ai "find files containing 'hello world'"

# List recent files
ai "show files modified today"

# Git operations
ai "show me git status and recent commits"
```

## Usage Modes

### Default Mode
Show command and ask for confirmation before executing:
```bash
ai "find python files"
# Output: Generated command: find . -name "*.py"
# Execute this command? (y/N):
```

### Display Mode
Just display the generated command without executing:
```bash
ai "show current date" -d
# Output: date
```

### Execute Mode
Automatically run the generated command without confirmation:
```bash
ai "show current date" -e
```

### Advanced: Shell Integration
For the best experience, set up shell integration with Cmd+G keybinding:

```bash
# Run the setup script
./setup_shell.sh

# Then use Cmd+G (or Ctrl+G) to activate AI command helper
# Type your request and review the generated command
```

## Command Options

- `-e`: Execute the generated command immediately without confirmation
- `-d`: Just display the generated command without executing
- `-c`: Show command and ask for confirmation (default behavior)
- No flags: Same as `-c` (confirm before executing)

## Examples

| Request | Generated Command |
|---------|------------------|
| `ai "find all python files"` | `find . -name "*.py" -type f` |
| `ai "disk usage"` | `du -sh .` |
| `ai "files modified today"` | `find . -type f -mtime -1` |
| `ai "search for hello"` | `grep -r "hello" .` |

## Requirements

- Python 3.7 or higher
- OpenAI API key
- Internet connection

## Troubleshooting

### "TERMAI_OPENAI_API_KEY not found" Error

If you get this error even after creating the `.env` file:

1. **Verify the .env file location:**
   ```bash
   ls -la ~/.env
   ```

2. **Check the .env file content:**
   ```bash
   head -c 20 ~/.env
   ```

3. **Force reinstall the package:**
   ```bash
   pip install --force-reinstall git+https://github.com/dan2labs/term-ai.git
   ```

4. **If using a virtual environment, make sure to install in the same environment:**
   ```bash
   source .venv/bin/activate  # or your venv path
   pip install git+https://github.com/dan2labs/term-ai.git
   ```

### "No module named 'dotenv'" Error

Install the required dependency:
```bash
pip install python-dotenv
```

### Command Not Found

If the `ai` command isn't found after installation:
```bash
# Check if it's installed
pip list | grep term-ai

# Reinstall if needed
pip install --force-reinstall git+https://github.com/dan2labs/term-ai.git
```

## Support

If you encounter any issues, please open an issue on GitHub. 
