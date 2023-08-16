class Task:
    def __init__(self, task_id, title, description, deadline, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed


class TaskRepository:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, deadline):
        task_id = len(self.tasks) + 1  # Генерируем уникальный идентификатор задачи
        task = Task(task_id, title, description, deadline)
        self.tasks.append(task)

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        task = self.get_task(task_id)
        if task:
            for key in kwargs:
                setattr(task, key, kwargs[key])
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
