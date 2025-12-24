@echo off
chcp 65001
cls

echo ============================================
echo     ТЕСТ РАБОТОСПОСОБНОСТИ CV-ASSISTANT
echo ============================================
echo.

echo 1. Проверка наличия Ollama...
where ollama >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Ollama найден
) else (
    echo ❌ Ollama не найден. Установите Ollama с https://ollama.com
    goto finish
)

echo.
echo 2. Проверка скрипта start_cv_assistant.ps1...
if exist "start_cv_assistant.ps1" (
    echo ✅ Скрипт start_cv_assistant.ps1 найден
) else (
    echo ❌ Скрипт start_cv_assistant.ps1 не найден
    goto finish
)

echo.
echo 3. Проверка скрипта run_switch.bat...
if exist "run_switch.bat" (
    echo ✅ Скрипт run_switch.bat найден
) else (
    echo ❌ Скрипт run_switch.bat не найден
    goto finish
)

echo.
echo 4. Проверка конфигурации Continue...
set CONTINUE_CONFIG_DIR=..\..\..\Configs\Continue
set SMART_SWITCH_PATH=%CONTINUE_CONFIG_DIR%\smart_switch.py

if exist "%SMART_SWITCH_PATH%" (
    echo ✅ Конфигурация Continue найдена
) else (
    echo ⚠️  Конфигурация Continue не найдена
    echo    Убедитесь, что папка Configs\Continue существует
)

echo.
echo ==================== РЕЗУЛЬТАТ ====================
echo.
echo Все основные компоненты присутствуют и готовы к работе.
echo Для запуска:
echo 1. Запустите start_cv_assistant.ps1 для запуска Ollama
echo 2. Запустите run_switch.bat для настройки модели

echo Тест завершен успешно!

:finish
pause