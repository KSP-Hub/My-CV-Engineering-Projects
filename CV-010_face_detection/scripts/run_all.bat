@echo off
REM Skript dlya zapuska vseh CV-010 skriptov

echo [1/3] Zapusk bazovoy detekcii...
python face_detection.py

echo.
echo [2/3] Zapusk detekcii v realnom vremeni...
echo Nazhmite 'q' posle testirovaniya
python real_time_detection.py

echo.
echo [3/3] Zapusk veb-interfeysa...
echo Pereydite v brauzere po adresu: http://localhost:5000
echo Nazhmite Ctrl+C dlya ostanovki servera
python CV-010-app.py & pause

echo.
echo [4/4] Zaversheno!
pause