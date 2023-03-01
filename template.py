import os
#from src.config import *

def create_structure():

    dirs = [
        os.path.join("data","raw"),
        os.path.join("data","preprocessed"),
        "notebooks",
        "saved_models",
        "logs",
        "src",
        os.path.join("src", "config")
    ]

    for dir_ in dirs:
        os.makedirs(dir_, exist_ok= True)
        with open(os.path.join(dir_, ".gitkeep"), "w") as f:
            pass 

    files = [
        "dvc.yaml",
        "params.yaml",
        ".gitignore",
        os.path.join("src", "__init__.py"),
        os.path.join("src", "config", "__init__.py")
    ]   

    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass

if __name__ == "__main__":
    create_structure()