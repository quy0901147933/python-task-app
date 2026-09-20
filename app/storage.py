import json 
from pathlib import Path 

DATA_FILE = Path(__file__).parent.parent / "tasks.json"


def load_tasks(path: Path = DATA_FILE) -> list[dict]:
    try:
        with open(path , "r" , encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: File task.json ne contient pas code JSON approprie")
        return []

def save_tasks(
    tasks: list[dict],
    path: Path = DATA_FILE,
) -> None:
    
    with open(path , "w" , encoding='utf-8') as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=2,
        )

