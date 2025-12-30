# AF Creative V2T Test

Test repository for Backline SCA vulnerability remediation testing.

This is a simplified test project based on a real customer repository structure.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Run the web server
python app.py run-server --port 5000

# Process data
python app.py process-data input.csv

# Load config
python app.py load-config config.yaml
```

## Purpose

This repository is used to test:
- Private PyPI registry support (--extra-index-url)
- Vulnerability detection and remediation
- Package upgrade workflows
