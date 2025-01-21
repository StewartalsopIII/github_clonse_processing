from setuptools import setup, find_packages

# Read requirements files
def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read transcript generator requirements
transcript_reqs = read_requirements('transcript_generator/requirements.txt')

# Read title generator requirements
title_reqs = read_requirements('title_generator/requirements.txt')

setup(
    name="process_recordings",
    version="0.1.0",
    author="Stewart Alsop",
    description="Tools for processing podcast recordings: transcription and title generation",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],  # Base requirements if any
    extras_require={
        "transcript": transcript_reqs,
        "title": title_reqs,
        "all": transcript_reqs + title_reqs
    },
)
