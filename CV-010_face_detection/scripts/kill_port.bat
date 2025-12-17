@echo off
:: Script to kill process using port 5000 and start the server
:: Created by AI Assistant

echo [1/3] Checking if port 5000 is in use...

:: Find process using port 5000
tasklist /FI "PID eq %PID%" 2>nul | find /I /N "PID" >nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5000" ^| findstr "LISTENING"') do (
    set "PID=%%a"
)

if defined PID (
    echo [2/3] Port 5000 is being used by process with PID %PID%
    
    :: Get process name
    for /f "tokens=2" %%a in ('tasklist /FI "PID eq %PID%" ^| findstr %PID%') do (
        set "PROC_NAME=%%a"
    )
    
    echo Found process: %PROC_NAME% (PID: %PID%)
    
    echo [3/3] Terminating process...
    taskkill /PID %PID% /F
    if errorlevel 1 (
        echo ERROR: Failed to terminate process
        exit /b 1
    )
    echo Process terminated successfully
) else (
    echo Port 5000 is free
)

echo.
echo Starting server...
python "D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/app.py"