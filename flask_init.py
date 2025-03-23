import os
import argparse

def create_flask_project(project_name):
    """Crée la structure de base d'un projet Flask."""
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
            "requirements.txt"
        ]
    }

    for folder, items in structure.items():
        for item in items:
            path = os.path.join(folder, item)
            if "." in item:  # Fichier
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    f.write("")  # Crée un fichier vide
            else:  # Dossier
                os.makedirs(path, exist_ok=True)

    print(f"✅ Projet Flask '{project_name}' créé avec succès !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère une structure de projet Flask.")
    parser.add_argument("project_name", help="Nom du projet Flask à créer")

    args = parser.parse_args()
    create_flask_project(args.project_name)
