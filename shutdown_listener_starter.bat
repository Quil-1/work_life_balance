@echo off

REM THIS SCRIPT RUNS THE SHUTDOWN LISTENER PYTHON SCRIPT 

for /f "delims=" %%p in ('where python') do (
    if not defined PYTHON_PATH (
        set "PYTHON_PATH=%%p"
    )
)

REM Set the directory of the batch script as the base directory
set BASE_DIR=%~dp0

REM Replace the script name with your Python script
set SCRIPT_NAME=shutdown_listener.py

REM Construct the full script path using the base directory and script name
set SCRIPT_PATH=%BASE_DIR%%SCRIPT_NAME%

@REM REM Start the shutdown listener service
REM Start the shutdown listener service in the background
start "Shutdown Listener Service" /MIN %PYTHON_PATH% %SCRIPT_PATH%

pause
