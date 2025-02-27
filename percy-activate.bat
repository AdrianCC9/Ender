@echo off
REM Change to the directory containing percy.py
cd /d Q:\Percy
REM Activate the virtual environment
call .percy-venv\Scripts\activate.bat
REM Run the Percy script
python percy_ui.py
