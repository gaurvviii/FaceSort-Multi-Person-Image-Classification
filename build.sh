#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "Virtual environment created."
fi

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install tensorflow numpy scikit-learn opencv-python matplotlib

# Create data and output directories
echo "Creating necessary directories..."
mkdir -p data
mkdir -p output

echo "Setup complete. You can now run your script using ./execute.sh"
