import sys
from .manager import TaskManager

def main():
    manager = TaskManager()
    
    if len(sys.argv) < 2:
        print("Uso: python -m src.cli [add|list|done] [argumento]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Debes proporcionar el texto de la tarea.")
            return
        title = " ".join(sys.argv[2:])
        task = manager.add_task(title)
        print(f"Tarea añadida con éxito [ID: {task['id']}]")

    elif command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No hay tareas registradas.")
            return
        print("\n--- Lista de Tareas ---")
        for t in tasks:
            status = "✓" if t["completed"] else " "
            print(f"[{status}] {t['id']}. {t['title']}")

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Indica el ID de la tarea a completar.")
            return
        try:
            task_id = int(sys.argv[2])
            if manager.complete_task(task_id):
                print(f"Tarea {task_id} marcada como completada.")
            else:
                print(f"No se encontró la tarea con ID {task_id}.")
        except ValueError:
            print("Error: El ID debe ser un número entero.")

if __name__ == "__main__":
    main()
