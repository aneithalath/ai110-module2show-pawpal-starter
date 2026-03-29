
import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_sorting_correctness():
    """Tasks are sorted chronologically by time."""
    t1 = Task("A", "09:00", "daily")
    t2 = Task("B", "07:30", "daily")
    t3 = Task("C", "12:00", "daily")
    tasks = [t1, t2, t3]
    scheduler = Scheduler(Owner("Test"))
    sorted_tasks = scheduler.sort_by_time(tasks)
    assert [t.description for t in sorted_tasks] == ["B", "A", "C"]

def test_recurrence_logic():
    """Completing a daily task creates a new one for the next day."""
    pet = Pet("Rex", "dog")
    task = Task("Walk", "08:00", "daily")
    pet.add_task(task)
    scheduler = Scheduler(Owner("Test"))
    scheduler.mark_task_complete(task, pet)
    # Original task is completed
    assert task.completed
    # New task is created
    assert len(pet.tasks) == 2
    # New task is not completed and has same description/time
    new_task = pet.tasks[-1]
    assert not new_task.completed
    assert new_task.description == "Walk"
    assert new_task.time == "08:00"

def test_conflict_detection():
    """Detects tasks with the same time."""
    t1 = Task("Feed", "09:00", "daily")
    t2 = Task("Walk", "09:00", "daily")
    tasks = [t1, t2]
    scheduler = Scheduler(Owner("Test"))
    warnings = scheduler.detect_conflicts(tasks)
    assert any("Conflict" in w for w in warnings)

def test_edge_case_no_tasks():
    """Scheduler methods handle pets with no tasks gracefully."""
    pet = Pet("Solo", "cat")
    owner = Owner("Test")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    # Should not crash, should return empty lists
    assert scheduler.sort_by_time([]) == []
    assert scheduler.filter_by_status([], completed=False) == []
    assert scheduler.detect_conflicts([]) == []
