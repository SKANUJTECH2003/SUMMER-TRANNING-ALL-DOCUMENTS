@echo off
cd /d "%~dp0"

set PYTHON_EXE=
if exist "%~dp0\.venv\Scripts\pythonw.exe" (
    set PYTHON_EXE="%~dp0\.venv\Scripts\pythonw.exe"
) else if exist "C:\Users\Anjali Vishawakarma\AppData\Local\Programs\Python\Python312\pythonw.exe" (
    set PYTHON_EXE="C:\Users\Anjali Vishawakarma\AppData\Local\Programs\Python\Python312\pythonw.exe"
)

if defined PYTHON_EXE (
    start "" %PYTHON_EXE% "%~dp0q12_online_shopping_system.py"
) else (
    echo Python launcher not found.
    pause
)
