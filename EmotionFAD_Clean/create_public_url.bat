@echo off
title FAD - Creating Public URL
color 0B

echo ============================================================
echo.
echo   Creating Public URL for FAD
echo.
echo ============================================================
echo.

REM Check if ngrok is installed
where ngrok >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] ngrok is not installed!
    echo.
    echo Please follow these steps:
    echo.
    echo 1. Download ngrok from: https://ngrok.com/download
    echo 2. Extract ngrok.exe to this folder
    echo 3. Sign up at: https://dashboard.ngrok.com/signup
    echo 4. Get your auth token
    echo 5. Run: ngrok config add-authtoken YOUR_TOKEN
    echo.
    echo After setup, run this script again.
    echo.
    pause
    exit /b 1
)

echo [OK] ngrok is installed!
echo.
echo Starting FAD server in background...
echo.

REM Start FAD server in a new window
start "FAD Server" cmd /k "python app.py"

echo Waiting for server to start...
timeout /t 5 /nobreak >nul

echo.
echo Starting ngrok tunnel...
echo.
echo ============================================================
echo.
echo   Your FAD application will be accessible via:
echo   https://[EmmotionFAD].ngrok.io
echo.
echo   Share this URL with anyone to give them access!
echo.
echo   Press Ctrl+C to stop the tunnel
echo.
echo ============================================================
echo.

REM Start ngrok
ngrok http 5000

REM If ngrok exits, cleanup
echo.
echo Tunnel closed. Stopping FAD server...
taskkill /FI "WindowTitle eq FAD Server*" /T /F >nul 2>nul
