#!/usr/bin/env bash
set -e

PROJECT_MAIN_DIR_NAME="SBY-backend"

# Validate variables
if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
    echo "Error: PROJECT_MAIN_DIR_NAME is not set. Please set it to your project directory name." >&2
    exit 1
fi

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Change directory to the project main directory
cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Activate virtual environment
source "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv/bin/activate"

# Restart Gunicorn and Nginx services
sudo service gunicorn restart
sudo service nginx restart

# Start API
cd $PROJECT_MAIN_DIR_NAME/
python3 manage.py runserver 0.0.0.0:8000