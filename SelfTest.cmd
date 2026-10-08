@echo off
setlocal
set ROOT=%~dp0
py -3.12 "%ROOT%windows\smoke_test.py" %*
exit /b %errorlevel%
