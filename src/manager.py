import json
import os

class TaskManager:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, title):
        task = {"id": len(self.tasks) + 1, "title": title, "completed": False}
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False
