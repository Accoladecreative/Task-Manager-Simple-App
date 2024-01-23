# main.py
from model.task_manager import TaskManager


def main():
    # Create a TaskManager instance
    task_manager = TaskManager()

    # Add tasks
    task_manager.add_task("Complete assignment")
    task_manager.add_task("Buy groceries")
    task_manager.add_task("Attend meeting")

    # Display the current tasks
    print("Current tasks:")
    for index, task in enumerate(task_manager.tasks, start=1):
        print(f"{index}. {task}")

    # Remove a task
    task_to_remove = "Buy groceries"
    task_manager.remove_task(task_to_remove)
    print(f"\nRemoved task: {task_to_remove}")

    # Display the updated tasks
    print("\nUpdated tasks:")
    for index, task in enumerate(task_manager.tasks, start=1):
        print(f"{index}. {task}")

    # Display the total number of tasks
    total_tasks = task_manager.get_task_count()
    print(f"\nTotal number of tasks: {total_tasks}")

    # Clear all tasks
    task_manager.clear_tasks()
    print("\nAll tasks cleared.")

    # Display the tasks after clearing
    print("\nRemaining tasks:")
    for index, task in enumerate(task_manager.tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    main()
