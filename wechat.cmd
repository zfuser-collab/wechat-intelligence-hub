@echo off
setlocal
set ROOT=%~dp0
set COMMAND=
if "%~1"=="" (
  echo Usage: wechat.cmd ^<reader^|hub^> [args]
  echo Example: wechat.cmd hub home
  echo          wechat.cmd reader status --pretty
  exit /b 1
)
set COMMAND=%~1
shift

if /I "%COMMAND%"=="reader" (
  py -3 "%ROOT%projects\rion-wechat-reader\rion_wechat_reader.py" %*
  exit /b %errorlevel%
)

if /I "%COMMAND%"=="hub" (
  py -3 "%ROOT%projects\wechat-intelligence-hub\wechat_intelligence_hub.py" %*
  exit /b %errorlevel%
)

echo Unsupported command: %COMMAND%
echo Supported commands: reader, hub
exit /b 2
