# test_task_manager.py
import sys
import os

# Add the path to the model directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.task_manager import TaskManager
import unittest

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Task 1")
        self.assertEqual(self.task_manager.get_task_count(), 1)

    def test_remove_task(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.remove_task("Task 1")
        self.assertEqual(self.task_manager.get_task_count(), 0)

    def test_get_task_count(self):
        self.assertEqual(self.task_manager.get_task_count(), 0)
        self.task_manager.add_task("Task 1")
        self.assertEqual(self.task_manager.get_task_count(), 1)

    def test_clear_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.clear_tasks()
        self.assertEqual(self.task_manager.get_task_count(), 0)

if __name__ == '__main__':
    unittest.main()