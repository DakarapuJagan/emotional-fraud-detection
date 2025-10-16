@echo off
title EmotionFAD - Fraud Activity Detection System
color 0A

echo ============================================================
echo.
echo   ███████╗███╗   ███╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
echo   ██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
echo   █████╗  ██╔████╔██║██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║
echo   ██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██║██║   ██║██║╚██╗██║
echo   ███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║
echo   ╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
echo.
echo   ███████╗ █████╗ ██████╗ 
echo   ██╔════╝██╔══██╗██╔══██╗
echo   █████╗  ███████║██║  ██║
echo   ██╔══╝  ██╔══██║██║  ██║
echo   ██║     ██║  ██║██████╔╝
echo   ╚═╝     ╚═╝  ╚═╝╚═════╝ 
echo.
echo   Fraud Activity Detection System
echo.
echo ============================================================
echo.
echo Starting EmotionFAD Server...
echo.
echo Browser will open automatically at http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ============================================================
echo.

cd /d "%~dp0"

python app.py

if errorlevel 1 (
    echo.
    echo ============================================================
    echo ERROR: Failed to start EmotionFAD
    echo ============================================================
    echo.
    echo Possible solutions:
    echo 1. Make sure Python is installed
    echo 2. Install dependencies: pip install -r requirements.txt
    echo 3. Check if port 5000 is available
    echo.
    pause
)
