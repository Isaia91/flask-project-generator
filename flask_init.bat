@echo off
set mypath=%cd%
if "%1"=="" (
    echo ❌ Erreur : Vous devez spécifier un nom de projet.
    echo Exemple : flask-init MonProjet
    exit /b
)
set path_to_python_script=%mypath%\flask_init.py
python %path_to_python_script% %1
