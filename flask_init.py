import os
import argparse

def create_flask_project(project_name):
    """Crée la structure de base d'un projet Flask avec des fichiers pré-remplis."""
    structure = {
        project_name: [
            "static",
            "templates",
            "app",
            "app/__init__.py",
            "app/routes.py",
            "app/models.py",
            "app/forms.py",
            "config.py",
            "run.py",
            "requirements.txt",
            "README.md"
        ]
    }

    # Création des dossiers et fichiers
    for folder, items in structure.items():
        for item in items:
            path = os.path.join(folder, item)
            if "." in item:  # Fichier
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    f.write(get_default_content(item))  # Ajoute du contenu de base
            else:  # Dossier
                os.makedirs(path, exist_ok=True)

    print(f"Projet Flask '{project_name}' créé avec succès !")

def get_default_content(filename):
    """Retourne du contenu de base pour certains fichiers."""
    if filename == "app/__init__.py":
        return "from flask import Flask\n\napp = Flask(__name__)\n\nfrom app import routes"
    
    if filename == "app/routes.py":
        return "from app import app\n\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\n"

    if filename == "run.py":
        return "from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)"

    if filename == "requirements.txt":
        return "Flask"

    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère une structure de projet Flask.")
    parser.add_argument("project_name", help="Nom du projet Flask à créer")
    args = parser.parse_args()
    create_flask_project(args.project_name)
