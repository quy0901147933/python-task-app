def complete_task(
    tasks: list[dict],
    task_id: int
) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True 
            return True 
    return False
def add_task(tasks: list[dict], title: str) -> None:
    title = title.strip()
    if not title:
        raise ValueError("Nom du travail ne permet pas d'etre vide")
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    task = {
        "id": new_id,
        "title": title,
        "done": False 
    }

    tasks.append(task)

def show_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("il n'y a pas n'importe boulot")
        return 
    for task in tasks:
        status = "Fini" if task["done"] else "Pas fini"
        print(
            f'{task["id"]}.{task["title"]} - {status}'
        )

def rename_task(
    tasks: list[dict],
    task_id: int,
    new_title: str,
) -> bool:
    new_title = new_title.strip()

    if not new_title:
        raise ValueError("Le titre ne peut pas être vide. ")
    
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            return True
    return False 
