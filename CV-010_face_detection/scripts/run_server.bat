@echo off
REM Skript dlya zapuska veb-servera CV-010

echo [1/2] Ustanovka zavisimostey (esli nuzhno)...
pip install -r requirements.txt

echo.
echo [2/2] Zapusk veb-interfeysa...
echo Pereydite v brauzere po adresu: http://localhost:5000
echo Nazhmite Ctrl+C dlya ostanovki servera
python CV-010-app.py

echo.
echo [3/3] Zaversheno!
pause