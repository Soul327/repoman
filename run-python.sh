#!/bin/bash

# Exit of error
set -e

PROJECT_PATH=./repos/reports
REQUIREMENTS="requirements.txt"

# Change to our project path
cd "$PROJECT_PATH"

# Check if the .venv directory exists
if [ -d ".venv" ]; then
	echo ".venv already exists."
else
	echo ".venv not found. Creating virtual environment..."
	python -m venv ".venv"
	echo "Virtual environment created in .venv."
fi

# Activate the virtual environment (works in Bash)
source ".venv/bin/activate"

# Install dependencies if requirements.txt exists
if [ -f "$REQUIREMENTS" ]; then
	echo "Installing dependencies from $REQUIREMENTS..."
	pip install -r "$REQUIREMENTS"
	echo "Dependencies installed."
else
	echo "No $REQUIREMENTS file found. Skipping dependency installation."
fi