# Process Recordings

A collection of tools for podcast production, including transcript generation and title suggestions.

## Installation

You can install the packages separately or together:

```bash
# Install just the transcript generator
pip install process_recordings[transcript]

# Install just the title generator
pip install process_recordings[title]

# Install everything
pip install process_recordings[all]
```

## Transcript Generator

Monitors a Dropbox folder for new podcast recordings and automatically generates transcripts.

```python
from process_recordings.transcript_generator import monitor
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up your Dropbox path
DROPBOX_PATH = "path/to/your/dropbox/folder"

# Start monitoring
monitor.monitor_folder(DROPBOX_PATH)
```

## Title Generator

Analyzes transcripts and suggests creative titles.

```python
from process_recordings.title_generator import analyzer
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables and configure AI
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')
title_analyzer = analyzer.TitleAnalyzer(model)

# Analyze a transcript
with open('transcript.txt', 'r') as f:
    transcript = f.read()

# Generate title suggestions
analysis = title_analyzer.analyze_transcript(transcript)

# Save the analysis
title_analyzer.save_analysis(analysis, 'title_suggestions.md')
```

## Requirements

### For Transcript Generator:
- Python 3.8+
- watchdog>=3.0.0
- python-dotenv>=1.0.0
- google-generativeai>=0.3.0
- tqdm>=4.66.1
- ffmpeg (system requirement for audio conversion)

### For Title Generator:
- Python 3.8+
- google-generativeai>=0.3.0
- python-dotenv>=1.0.0

## Environment Variables

Create a `.env` file with:
```
GOOGLE_API_KEY=your_api_key_here
```

## Directory Structure

```
process_recordings/
├── transcript_generator/
│   ├── src/
│   │   ├── __init__.py
│   │   └── monitor.py
│   └── requirements.txt
├── title_generator/
│   ├── src/
│   │   ├── __init__.py
│   │   └── analyzer.py
│   └── requirements.txt
└── setup.py
```

## Development

To set up for development:

```bash
# Clone the repository
git clone <repository-url>

# Install in development mode
pip install -e ".[all]"
```

## Using Both Tools Together

You can also use both tools together to automatically process new recordings:

```python
from process_recordings.transcript_generator import monitor
from process_recordings.title_generator import analyzer
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro')

# Initialize title analyzer
title_analyzer = analyzer.TitleAnalyzer(model)

# Configure monitoring with title generation
DROPBOX_PATH = "path/to/your/dropbox/folder"
monitor.monitor_folder(DROPBOX_PATH)
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.