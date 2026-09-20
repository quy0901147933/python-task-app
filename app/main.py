from app.tasks import complete_task, add_task, show_tasks
from app.storage import load_tasks, save_tasks
def main() -> None:
    tasks = load_tasks()

    print("\nGerer travail")
    print("1. Ajouter travail")
    print("2. Finaliser travail")
    print("3. Afficher la liste")
    print("0. Exit")

    choice = input("Tu choissit: ").strip()

    if choice == "1":
        title = input("Nom de nouvel travail: ")

        try:
            add_task(tasks, title)
            save_tasks(tasks)
            print("Deja ajoute et sauvergarde travail")
        except ValueError as error:
            print(f"Error: {error}")
    elif choice == "2":
        try:
            task_id = int(input("ID pour completer : "))
        except ValueError:
            print("Vous avez besoin d'un integer")
            return 
        found = complete_task(tasks, task_id)

        if found:
            save_tasks(tasks)
            print("Deja finalise travail")
        else:
            print("Ne pas finaliser ou trouver ID")

    elif choice == "3":
        show_tasks(tasks)
    elif choice == "0":
        print("Deja quitte programme")
    else:
        print("Choice n'est pas valuable")


if __name__ == "__main__":
    main()


