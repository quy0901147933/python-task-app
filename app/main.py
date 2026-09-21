from app.tasks import complete_task, add_task, show_tasks, rename_task
from app.storage import load_tasks, save_tasks
def main() -> None:
    tasks = load_tasks()

    print("\nGerer travail")
    print("1. Ajouter travail")
    print("2. Finaliser travail")
    print("3. Afficher la liste")
    print("4. Renommer un travail")
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
            print("Ne pas trouver ID")

    elif choice == "3":
        show_tasks(tasks)
    elif choice == "4":
        try:
            task_id = int(input("Saissir ID du travail af renommer : "))
        except:
            print("L'ID doit etre un nombre entier.")
        
        new_title = input("Saissir le nom du travail: ")
        try:
            found = rename_task(tasks, task_id, new_title )
        except ValueError as error:
            print(f"Erreur : {error}")
            return
        
        if found:
            save_tasks(tasks)
            print("Travail defa renomme et sauvegarde.")
        else:
            print("ID introuvable. ")

    elif choice == "0":
        print("Deja quitte programme")
    else:
        print("Choice n'est pas valuable")



if __name__ == "__main__":
    main()


