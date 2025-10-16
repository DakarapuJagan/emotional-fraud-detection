@echo off
title EmotionFAD - Upload to GitHub
color 0A

echo ============================================================
echo.
echo   EmotionFAD - GitHub Upload
echo.
echo ============================================================
echo.

REM Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git:
    echo 1. Download from: https://git-scm.com/download/win
    echo 2. Install with default settings
    echo 3. Restart this script
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed!
echo.

REM Check if already a git repository
if exist ".git" (
    echo [INFO] This is already a Git repository.
    echo.
    goto :push_changes
)

echo [STEP 1] Initializing Git repository...
git init
echo.

echo [STEP 2] Adding all files...
git add .
echo.

echo [STEP 3] Creating first commit...
git commit -m "Initial commit - EmotionFAD Fraud Detection System"
echo.

echo ============================================================
echo.
echo   Now you need to create a GitHub repository:
echo.
echo   1. Go to: https://github.com/new
echo   2. Repository name: EmotionFAD
echo   3. Description: AI-powered fraud detection system
echo   4. Make it Public or Private
echo   5. DO NOT initialize with README
echo   6. Click "Create repository"
echo.
echo   After creating, copy the repository URL
echo   Example: https://github.com/yourusername/EmotionFAD.git
echo.
echo ============================================================
echo.

set /p REPO_URL="Paste your GitHub repository URL here: "

if "%REPO_URL%"=="" (
    echo [ERROR] No URL provided!
    pause
    exit /b 1
)

echo.
echo [STEP 4] Linking to GitHub repository...
git remote add origin %REPO_URL%
echo.

echo [STEP 5] Pushing to GitHub...
git branch -M main
git push -u origin main
echo.

echo ============================================================
echo.
echo   SUCCESS! Your EmotionFAD project is now on GitHub!
echo.
echo   View it at: %REPO_URL%
echo.
echo ============================================================
echo.
pause
exit /b 0

:push_changes
echo [INFO] Pushing latest changes...
echo.

git add .
git commit -m "Update EmotionFAD - %date% %time%"
git push origin main

echo.
echo ============================================================
echo.
echo   SUCCESS! Changes pushed to GitHub!
echo.
echo ============================================================
echo.
pause
