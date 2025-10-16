@echo off
echo Starting EmotionFAD - Emotion Analysis...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.7 or later from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Install required packages
echo Installing required packages...
pip install flask flask-socketio opencv-python fer numpy pillow python-dotenv

if %ERRORLEVEL% neq 0 (
    echo Error installing required packages.
    pause
    exit /b 1
)

echo.
echo Downloading emotion detection model (this may take a while)...
python -c "from fer import FER; detector = FER()"

if %ERRORLEVEL% neq 0 (
    echo Warning: Could not download emotion detection model automatically.
    echo The application may not work correctly.
    pause
)

echo.
echo Starting the application...
echo.
echo Open your web browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

:: Create necessary directories
mkdir uploads 2>nul

:: Run the application
python app_emotion.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo An error occurred while running the application.
    echo.
    echo Troubleshooting:
    echo 1. Make sure port 5000 is not in use by another application
    echo 2. Try running this script as administrator
    echo 3. Check your firewall settings
    echo 4. Make sure you have a working internet connection for the first run
    echo.
    pause
)
