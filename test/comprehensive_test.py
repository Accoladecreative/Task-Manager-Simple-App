# test_comprehensive.py
import sys
import os

# Add the path to the model directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from model.task_manager import TaskManager

@pytest.fixture
def task_manager_instance():
    return TaskManager()

def test_add_task(task_manager_instance):
    task_manager_instance.add_task("Task 1")
    assert "Task 1" in task_manager_instance.tasks

def test_remove_task(task_manager_instance):
    task_manager_instance.add_task("Task 1")
    task_manager_instance.remove_task("Task 1")
    assert "Task 1" not in task_manager_instance.tasks

def test_remove_nonexistent_task_raises_error(task_manager_instance):
    with pytest.raises(ValueError):
        task_manager_instance.remove_task("Nonexistent Task")

def test_get_task_count(task_manager_instance):
    task_manager_instance.add_task("Task 1")
    task_manager_instance.add_task("Task 2")
    assert task_manager_instance.get_task_count() == 2

def test_clear_tasks(task_manager_instance):
    task_manager_instance.add_task("Task 1")
    task_manager_instance.clear_tasks()
    assert task_manager_instance.get_task_count() == 0

def test_clear_empty_tasks(task_manager_instance):
    task_manager_instance.clear_tasks()
    assert task_manager_instance.get_task_count() == 0

def test_integration_scenario(task_manager_instance):
    task_manager_instance.add_task("Task 1")
    task_manager_instance.add_task("Task 2")
    
    assert task_manager_instance.get_task_count() == 2
    assert "Task 1" in task_manager_instance.tasks
    assert "Task 2" in task_manager_instance.tasks

    task_manager_instance.remove_task("Task 1")

    assert task_manager_instance.get_task_count() == 1
    assert "Task 1" not in task_manager_instance.tasks
    assert "Task 2" in task_manager_instance.tasks

    task_manager_instance.clear_tasks()

    assert task_manager_instance.get_task_count() == 0
    assert not task_manager_instance.tasks

def test_empty_task_manager_properties(task_manager_instance):
    assert task_manager_instance.get_task_count() == 0
    assert not task_manager_instance.tasks

def test_add_remove_tasks_with_different_data_types(task_manager_instance):
    task_manager_instance.add_task("String Task")
    task_manager_instance.add_task(123)
    task_manager_instance.add_task(["List Task"])

    assert task_manager_instance.get_task_count() == 3
    assert "String Task" in task_manager_instance.tasks
    assert 123 in task_manager_instance.tasks
    assert ["List Task"] in task_manager_instance.tasks

def test_performance_with_large_number_of_tasks(task_manager_instance):
    for i in range(1000):
        task_manager_instance.add_task(f"Task {i}")

    assert task_manager_instance.get_task_count() == 1000

    for i in range(500):
        task_manager_instance.remove_task(f"Task {i}")

    assert task_manager_instance.get_task_count() == 500
