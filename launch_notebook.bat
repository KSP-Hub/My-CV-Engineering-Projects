@echo off
REM Avtomaticheskiy zapusk Jupyter Notebook
echo Zapusk Jupyter Notebook...
echo.
echo Proekt: My-CV-Engineering-Projects
echo Put: D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects
echo.
echo Ozhidanie zapuska...

jupyter notebook --notebook-dir="D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects"

echo Esli okno zakrylos, prover:
- Ustanovlen li  Jupyter: pip install jupyter
- Dostupen li Python v komandnoy stroke
pause