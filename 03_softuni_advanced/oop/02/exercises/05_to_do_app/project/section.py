from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        task_to_complete = next((t for t in self.tasks if t.name == task_name), None)
        if task_to_complete:
            task_to_complete.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]

        return f"Cleared {len(removed_tasks)} tasks."

    def view_section(self) -> str:
        result = [f"Section {self.name}:"]
        result.extend([task.details() for task in self.tasks])
        return "\n".join(result)
