# tests/test_pawpal.py
import pytest
from pawpal_system import Task, Pet

def test_task_completion():
    """Test that mark_complete sets completed to True."""
    task = Task("Test Task", "09:00", "daily")
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_task_addition():
    """Test that adding a task increases pet's task list."""
    pet = Pet("TestPet", "dog")
    initial_count = len(pet.tasks)
    task = Task("Test Task", "09:00", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[-1] == task
