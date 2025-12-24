@echo off
chcp 65001
cls
echo.
echo ============================================
echo     ПЕРЕКЛЮЧАТЕЛЬ МОДЕЛЕЙ Continue
echo ============================================
echo.

:: Убедитесь что путь правильный!
set SCRIPT_DIR=%~dp0
set SMART_SWITCH_PATH=%SCRIPT_DIR%\..\..\..\Configs\Continue\smart_switch.py

if exist "%SMART_SWITCH_PATH%" (
    python "%SMART_SWITCH_PATH%"
) else (
    echo.
    echo ОШИБКА: Файл smart_switch.py не найден!
    echo Проверьте путь: %SMART_SWITCH_PATH%
    echo Убедитесь, что папка Configs\Continue существует в корне проекта.
    pause
    exit /b 1
)

pause
