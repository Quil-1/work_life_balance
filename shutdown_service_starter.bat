@echo off

set SCRIPT_NAME=shutdown_service.py

REM Getting the installation directory of python executable
for /f "delims=" %%p in ('where python') do (
    if not defined PYTHON_PATH (
        set "PYTHON_PATH=%%p"
    )
)

REM Set the directory of the batch script as the base directory
set BASE_DIR=%~dp0

REM Construct the full script path using the base directory and script name
set SCRIPT_PATH=%BASE_DIR%%SCRIPT_NAME%

REM Install the service
%PYTHON_PATH% %SCRIPT_PATH% --startup auto install

REM Start the service
%PYTHON_PATH% %SCRIPT_PATH% start

pause
