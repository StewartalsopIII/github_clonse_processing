#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import google.generativeai as genai
from transcript_generator.monitor import monitor_folder

# Load environment variables
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Get Dropbox path from environment variables
DROPBOX_PATH = os.getenv('DROPBOX_PATH')

if not DROPBOX_PATH:
    raise ValueError("DROPBOX_PATH not set in .env file")

if __name__ == "__main__":
    print(f"Starting to monitor: {DROPBOX_PATH}")
    print("Waiting for new recordings...")
    monitor_folder(DROPBOX_PATH)
