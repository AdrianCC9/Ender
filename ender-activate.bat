@echo off
REM Change to the directory containing percy.py
cd /d Q:\Ender
REM Activate the virtual environment
call .ender-venv\Scripts\activate.bat
REM Run the Ender script
python ender_ui.py
