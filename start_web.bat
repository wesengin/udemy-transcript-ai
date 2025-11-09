@echo off
echo Starting Udemy Transcript Downloader Web Interface...
echo.

python app.py

if errorlevel 1 (
    echo.
    echo Error starting the application!
    echo Make sure you have installed all dependencies with setup.bat
    pause
)
