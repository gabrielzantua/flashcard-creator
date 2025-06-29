@echo off
echo Starting Flashcard Creator...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import customtkinter" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install customtkinter
)

REM Run the application
echo Launching Flashcard Creator...
python templater.py

pause 