class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = 'completed' if self.completed else 'Not completed'
        return f"Task ID: {self.id}, Description: {self.description}, status: {status}"
    
class ToDolist:
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def add_task(self, description):
        task = Task(self.current_id, description)
        self.tasks.append(task)
        self.current_id += 1
    
    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.id ==task_id:
             task.mark_as_completed()
            exit
        else:    
         print(f"No task with ID {task_id}")

    def display_tasks(self):
       if not self.tasks:
          print("No tasks in the list.")
       else:
          for task in self.tasks:
             print(task)

todo_list = ToDolist()
todo_list.add_task("Complete Python project")
todo_list.add_task("Go grocery shopping")
todo_list.add_task("Read a book")

print("Initial list of tasks:")
todo_list.display_tasks()

todo_list.mark_task_as_completed(2)

print("\nUpdated list of tasks:")
todo_list.display_tasks()