import customtkinter as ctk
from task import TaskRepository

class TodoAppGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Приложение для отслеживания задач")

        self.task_repository = TaskRepository()

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self.root, text="Добро пожаловать в приложение для отслеживания задач!")
        self.label.pack()

        self.title_entry = ctk.CTkEntry(self.root, placeholder_text="Заголовок")
        self.title_entry.pack()

        self.description_entry = ctk.CTkEntry(self.root, placeholder_text="Описание")
        self.description_entry.pack()

        self.deadline_entry = ctk.CTkEntry(self.root, placeholder_text="Срок выполнения (гггг-мм-дд)")
        self.deadline_entry.pack()

        self.create_button = ctk.CTkButton(self.root, text="Создать задачу", command=self.create_task)
        self.create_button.pack()

        self.get_task_entry = ctk.CTkEntry(self.root, placeholder_text="ID задачи")
        self.get_task_entry.pack()

        self.get_task_button = ctk.CTkButton(self.root, text="Получить задачу", command=self.get_task)
        self.get_task_button.pack()

        self.get_all_tasks_button = ctk.CTkButton(self.root, text="Получить все задачи", command=self.get_all_tasks)
        self.get_all_tasks_button.pack()

        self.update_task_entry = ctk.CTkEntry(self.root, placeholder_text="ID задачи")
        self.update_task_entry.pack()

        self.update_entries = []
        self.update_labels = []
        self.update_buttons = []

        for field in ["title", "description", "deadline"]:
            label = ctk.CTkLabel(self.root, text=f"{field.capitalize()}:")
            label.pack()
            self.update_labels.append(label)

            entry = ctk.CTkEntry(self.root, placeholder_text=field.capitalize())
            entry.pack()
            self.update_entries.append(entry)

        self.update_button = ctk.CTkButton(self.root, text="Обновить задачу", command=self.update_task)
        self.update_button.pack()

        self.delete_task_entry = ctk.CTkEntry(self.root, placeholder_text="ID задачи")
        self.delete_task_entry.pack()

        self.delete_task_button = ctk.CTkButton(self.root, text="Удалить задачу", command=self.delete_task)
        self.delete_task_button.pack()

    def create_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()

        self.task_repository.create_task(title, description, deadline)
        print("Успех", "Задача создана успешно!")

    def get_task(self):
        task_id = int(self.get_task_entry.get())
        task = self.task_repository.get_task(task_id)
        if task:
            print("Задача", f"ID: {task.task_id} Заголовок: {task.title}Описание: {task.description}Срок выполнения: {task.deadline}")
        else:
           print("Ошибка", "Задача не найдена!")

    def get_all_tasks(self):
        tasks = self.task_repository.get_all_tasks()
        task_info = "".join([f"ID: {task.task_id}, Заголовок: {task.title}" for task in tasks])
        print("Все задачи", task_info)

    def update_task(self):
        task_id = int(self.update_task_entry.get())
        updates = {label.cget("text").lower(): entry.get() for label, entry in zip(self.update_labels, self.update_entries)}
        success = self.task_repository.update_task(task_id, **updates)
        if success:
            print("Успех", "Задача обновлена успешно!")
        else:
            print("Ошибка", "Задача не найдена!")

    def delete_task(self):
        task_id = int(self.delete_task_entry.get())
        success = self.task_repository.delete_task(task_id)
        if success:
            print("Успех", "Задача удалена успешно!")
        else:
            print("Ошибка", "Задача не найдена!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TodoAppGUI()
    app.run()