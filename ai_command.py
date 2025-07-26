#!/usr/bin/env python3

import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        print("Please create a .env file with your OpenAI API key")
        return False
    print("✅ Environment loaded successfully")
    return True

def init_openai_client():
    """Initialize and return OpenAI client"""
    try:
        client = OpenAI()
        print("✅ OpenAI client initialized successfully")
        return client
    except Exception as e:
        print(f"❌ Error initializing OpenAI client: {e}")
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
        print(f"❌ Error generating command: {e}")
        return None

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='AI-powered terminal command generator')
    parser.add_argument('request', nargs='+', help='Natural language request for shell command')
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
                print(result)
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main() 