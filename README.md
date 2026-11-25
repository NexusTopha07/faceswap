
# AI Face Studio

A responsive AI video project interface built with
HTML, CSS, JavaScript and Python Flask.

## Features

- No user login or registration
- Image upload and preview
- Video upload and preview
- Consent confirmation
- Upload validation
- Temporary media storage
- Automatic cleanup of expired files
- Flask REST API

## Installation

### 1. Install Python

Install Python 3.11 or newer.

### 2. Create virtual environment

Windows:

python -m venv venv

### 3. Activate environment

venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Start the server

python app.py

### 6. Open website

http://127.0.0.1:5000

## Current status

Frontend and upload API are implemented.

AI processing is not connected yet.

## Privacy

Uploaded files are stored temporarily.
Files older than the configured retention
period are cleaned up when the upload API
is accessed again.

Do not use private media without permission.
