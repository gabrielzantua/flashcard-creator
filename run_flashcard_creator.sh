#!/bin/bash

echo "Starting Flashcard Creator..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

# Check if required packages are installed
if ! python3 -c "import customtkinter" &> /dev/null; then
    echo "Installing customtkinter..."
    pip3 install customtkinter
fi
if ! python3 -c "import PIL" &> /dev/null; then
    echo "Installing Pillow..."
    pip3 install pillow
fi

# Run the application
echo "Launching Flashcard Creator..."
python3 templater.py 