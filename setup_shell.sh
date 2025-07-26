#!/bin/bash

echo "Setting up AI command integration for your shell..."

# Detect shell
if [[ -n "$ZSH_VERSION" ]]; then
    SHELL_CONFIG="$HOME/.zshrc"
    SHELL_NAME="zsh"
elif [[ -n "$BASH_VERSION" ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
    SHELL_NAME="bash"
else
    echo "Unsupported shell. Please manually add the function to your shell config."
    exit 1
fi

# Create the shell function
SHELL_FUNCTION='
# AI command helper function
ai_populate() {
    local request
    echo -n "AI Command: "
    read request
    if [[ -n "$request" ]]; then
        ai "$request"
    fi
}

# Bind to Cmd+G
if [[ -n "$ZSH_VERSION" ]]; then
    bindkey "^G" ai_populate
elif [[ -n "$BASH_VERSION" ]]; then
    bind -x "\"\\C-g\":ai_populate"
fi
'

echo "Adding AI command function to $SHELL_CONFIG..."
echo "$SHELL_FUNCTION" >> "$SHELL_CONFIG"

echo "✅ Setup complete!"
echo ""
echo "Usage:"
echo "1. Press Cmd+G (or Ctrl+G) to activate the AI command helper"
echo "2. Type your request and press Enter"
echo "3. Review the generated command and confirm execution"
echo ""
echo "Alternative modes:"
echo "  ai \"your request\" -d    # Just show the command"
echo "  ai \"your request\" -e    # Execute without confirmation"
echo ""
echo "Please restart your terminal or run: source $SHELL_CONFIG" 