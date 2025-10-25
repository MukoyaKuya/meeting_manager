#!/usr/bin/env bash
# Exit if a command exits with a non-zero status.
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files (no user input)
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate
