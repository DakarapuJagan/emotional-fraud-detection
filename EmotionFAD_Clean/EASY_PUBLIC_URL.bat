@echo off
title EmotionFAD - Creating Public URL
color 0A

echo ============================================================
echo.
echo   EmotionFAD - Public URL Setup
echo.
echo ============================================================
echo.

REM Check if ngrok is installed
where ngrok >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] ngrok is not installed or not in PATH!
    echo.
    echo Quick Setup:
    echo 1. Download: https://ngrok.com/download
    echo 2. Extract ngrok.exe to this folder
    echo 3. Sign up: https://dashboard.ngrok.com/signup
    echo 4. Run: ngrok config add-authtoken YOUR_TOKEN
    echo.
    pause
    exit /b 1
)

echo [STEP 1] Checking ngrok configuration...
echo.

REM Check if configured
ngrok config check >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] ngrok is not configured!
    echo.
    echo Please run:
    echo   ngrok config add-authtoken YOUR_TOKEN
    echo.
    echo Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken
    echo.
    pause
    exit /b 1
)

echo [OK] ngrok is configured!
echo.

echo [STEP 2] Starting EmotionFAD server...
echo.

REM Kill any existing Python processes on port 5000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5000 ^| findstr LISTENING') do (
    echo Stopping existing server on port 5000...
    taskkill /F /PID %%a >nul 2>nul
)

REM Start EmotionFAD in a new window
start "EmotionFAD Server" /MIN cmd /c "python app.py"

echo Waiting for server to start...
timeout /t 8 /nobreak >nul

echo.
echo [STEP 3] Creating public URL with ngrok...
echo.
echo ============================================================
echo.
echo   IMPORTANT: Keep this window open!
echo.
echo   Your EmotionFAD will be accessible at:
echo   https://[random-id].ngrok.io
echo.
echo   Copy the URL and share it with anyone!
echo   Works on any device, any browser (Chrome, Edge, Safari, etc.)
echo.
echo   Press Ctrl+C to stop
echo.
echo ============================================================
echo.

REM Start ngrok with free random URL
ngrok http 5000

REM Cleanup when ngrok stops
echo.
echo Stopping EmotionFAD server...
taskkill /FI "WindowTitle eq EmotionFAD Server*" /T /F >nul 2>nul
echo.
echo Done!
pause
