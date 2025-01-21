#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import google.generativeai as genai
from transcript_generator.src.monitor import monitor_folder

# Load environment variables
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Your Dropbox folder path - this is where it will look for new recordings
DROPBOX_PATH = "/Users/stewartalsop/Dropbox/Crazy Wisdom/Beautifully Broken/Zoom Folder"

if __name__ == "__main__":
    print(f"Starting to monitor: {DROPBOX_PATH}")
    print("Waiting for new recordings...")
    monitor_folder(DROPBOX_PATH)
