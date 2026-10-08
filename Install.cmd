@echo off
setlocal
set ROOT=%~dp0

where py >nul 2>nul
if errorlevel 1 (
  echo Python 3.12+ is required for the Windows runner.
  echo Install Python 3.12.x from https://www.python.org/downloads/windows/
  exit /b 1
)

py -3.12 -c "import sys; print(sys.version_info[:2])" >nul 2>nul
if errorlevel 1 (
  echo Python 3.12.x was not found on PATH. Please install it and retry.
  exit /b 1
)

mkdir "%ROOT%.runtime" 2>nul
py -3.12 "%ROOT%windows\install_windows.py" %*
if errorlevel 1 exit /b %errorlevel%

echo.
echo Windows setup complete.
echo.
echo Next steps:
echo   SelfTest.cmd

echo   wechat.cmd hub home
