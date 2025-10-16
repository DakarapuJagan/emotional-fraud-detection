@echo off
echo Starting EmotionFAD Application...
echo.

echo Installing required packages...
pip install -r requirements_new.txt

if %ERRORLEVEL% neq 0 (
    echo Error installing requirements. Please check your Python and pip installation.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo Starting the application...
set FLASK_APP=app_new.py
set FLASK_ENV=development

python -m flask run --host=0.0.0.0 --port=5000

if %ERRORLEVEL% neq 0 (
    echo.
    echo Error starting the application. Please check the error message above.
    pause
    exit /b %ERRORLEVEL%
)

pause
