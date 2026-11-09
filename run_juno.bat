@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 -m pip install -r requirements.txt
  if errorlevel 1 goto failed
  py -3 juno_app.py
) else (
  python -m pip install -r requirements.txt
  if errorlevel 1 goto failed
  python juno_app.py
)
if errorlevel 1 goto failed
goto end
:failed
echo.
echo Juno could not start. Install Python 3.10 or newer from https://www.python.org/downloads/windows/
echo During setup, enable "Add Python to PATH", then run this file again.
pause
:end
endlocal
