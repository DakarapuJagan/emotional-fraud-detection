@echo off
echo Starting Simple EmotionFAD...
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
pip install flask flask-socketio eventlet

if %ERRORLEVEL% neq 0 (
    echo Error installing required packages.
    pause
    exit /b 1
)

echo.
echo Starting the application...
echo.
echo Open your web browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

:: Run the application
python simple_app.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo An error occurred while running the application.
    echo.
    echo Troubleshooting:
    echo 1. Make sure port 5000 is not in use by another application
    echo 2. Try running this script as administrator
    echo 3. Check your firewall settings
    echo.
    pause
)
