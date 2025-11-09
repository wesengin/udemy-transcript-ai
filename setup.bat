@echo off
echo ========================================
echo Udemy Transcript Downloader - Web Setup
echo ========================================
echo.

echo [1/3] Installing Node.js dependencies...
call npm install
if errorlevel 1 (
    echo Error installing Node.js dependencies
    pause
    exit /b 1
)

echo.
echo [2/3] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing Python dependencies
    pause
    exit /b 1
)

echo.
echo [3/3] Creating directories...
if not exist "output" mkdir output
if not exist "combined_transcripts" mkdir combined_transcripts
if not exist "summaries" mkdir summaries

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To start the web application, run:
echo   npm run web
echo.
echo Or directly with Python:
echo   python app.py
echo.
echo The application will be available at:
echo   http://localhost:5000
echo.
pause
