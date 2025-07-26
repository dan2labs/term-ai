#!/usr/bin/env python3

import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI

def load_environment():
    """Load environment variables from .env file"""
    # Try to load from home directory first, then current directory
    home_env = os.path.expanduser("~/.env")
    if os.path.exists(home_env):
        load_dotenv(home_env)
    else:
        load_dotenv()  # Try current directory
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        print("Please create a .env file in your home directory (~/.env) with your OpenAI API key")
        return False
    return True

def init_openai_client():
    """Initialize and return OpenAI client"""
    try:
        client = OpenAI()
        return client
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        return None

def generate_command(client, user_request):
    """Generate a shell command from natural language request"""
    try:
        prompt = f"""You are a helpful terminal assistant. Convert this request into a single shell command:

Request: {user_request}

Return ONLY the shell command, nothing else. Make it safe and efficient."""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful terminal assistant that generates safe shell commands."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.1
        )
        
        command = response.choices[0].message.content.strip()
        return command
    except Exception as e:
        print(f"Error generating command: {e}")
        return None

def populate_terminal_input(command):
    """Populate the terminal input buffer with the generated command"""
    try:
        print(command)
        return True
    except Exception as e:
        print(command)
        return False

def execute_command(command, confirm=False):
    """Execute a shell command with optional confirmation"""
    if confirm:
        print(f"Generated command: {command}")
        response = input("Execute this command? (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Command execution cancelled.")
            return False
    
    try:
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"Error executing command: {e}")
        return False

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='AI-powered terminal command generator')
    parser.add_argument('request', nargs='+', help='Natural language request for shell command')
    parser.add_argument('-e', action='store_true', help='Execute the generated command immediately')
    parser.add_argument('-d', action='store_true', help='Just display the command without executing')
    parser.add_argument('-c', action='store_true', help='Show command and ask for confirmation (default)')
    return parser.parse_args()

def main():
    """Main function for the console script entry point"""
    args = parse_arguments()
    user_request = ' '.join(args.request)
    
    if load_environment():
        client = init_openai_client()
        if client:
            result = generate_command(client, user_request)
            if result:
                if args.e:
                    execute_command(result, confirm=False)
                elif args.d:
                    print(result)
                else:
                    execute_command(result, confirm=True)
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main() 