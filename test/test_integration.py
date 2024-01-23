# test_integration.py
import sys
import os

# Add the path to the model directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from model.task_manager import TaskManager

def test_task_manager_integration():
    # Create a TaskManager instance
    task_manager = TaskManager()

    # Add tasks
    task_manager.add_task("Task 1")
    task_manager.add_task("Task 2")

    # Verify the count of tasks
    assert task_manager.get_task_count() == 2

    # Verify tasks
    assert "Task 1" in task_manager.tasks
    assert "Task 2" in task_manager.tasks

    # Remove a task
    task_manager.remove_task("Task 1")

    # Verify the updated count of tasks
    assert task_manager.get_task_count() == 1

    # Verify remaining tasks
    assert "Task 1" not in task_manager.tasks
    assert "Task 2" in task_manager.tasks

    # Clear all tasks
    task_manager.clear_tasks()

    # Verify the count of tasks after clearing
    assert task_manager.get_task_count() == 0

    # Verify that the tasks list is empty
    assert not task_manager.tasks