@echo off
if "%1"=="" (
    echo ❌ Erreur : Vous devez spécifier un nom de projet.
    echo Exemple : flask-init MonProjet
    exit /b
)
python C:\Users\isaia\scripts\python\flask\generateFlaskProject\flask_init.py %1
