from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    medical_needs: Optional[str] = None
    preferences: Optional[str] = None

    def update_info(self, **kwargs):
        pass

    def get_summary(self):
        pass

@dataclass
class Task:
    name: str
    type: str
    duration: int
    priority: int
    scheduled_time: Optional[str] = None
    notes: Optional[str] = None
    pet: Optional[Pet] = None  # Reference to the pet this task is for

    def edit_task(self, **kwargs):
        pass

    def mark_complete(self):
        pass

    def reschedule(self, new_time: str):
        pass

class Owner:
    def __init__(self, name: str, available_time: str, preferences: Optional[str] = None, contact_info: Optional[str] = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences
        self.contact_info = contact_info
        self.pets: List[Pet] = []

    def update_info(self, **kwargs):
        pass

    def set_preferences(self, preferences: str):
        pass

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        self.pets.remove(pet)

@dataclass
class Planner:
    owner: Owner
    pets: List[Pet]
    tasks: List[Task] = field(default_factory=list)
    date: Optional[str] = None
    constraints: Optional[str] = None

    def generate_plan(self):
        pass

    def explain_plan(self):
        pass

    def get_tasks_for_day(self, date: Optional[str] = None):
        pass

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        self.tasks.remove(task)
