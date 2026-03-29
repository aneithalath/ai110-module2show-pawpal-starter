from datetime import datetime
from typing import List

class Task:
    """Represents a pet care task."""
    def __init__(self, description: str, time: str, frequency: str, completed: bool = False):
        self.description = description
        self.time = time  # Store as string for simplicity, e.g., "08:00"
        self.frequency = frequency
        self.completed = completed


    def mark_complete(self):
        """Set this task as completed."""
        self.completed = True


    def __str__(self):
        """Return a readable string for the task."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.time} - {self.description} ({self.frequency})"

class Pet:
    """Represents a pet with a list of tasks."""
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.tasks: List[Task] = []


    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)


    def get_tasks(self) -> List[Task]:
        """Get all tasks for this pet."""
        return self.tasks


    def __str__(self):
        """Return a readable string for the pet."""
        return f"{self.name} the {self.species}"

class Owner:
    """Represents a pet owner with multiple pets."""
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []


    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)


    def get_all_tasks(self) -> List[Task]:
        """Get all tasks from all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


    def __str__(self):
        """Return a readable string for the owner."""
        return f"Owner: {self.name}"

class Scheduler:
    """Schedules and formats tasks for an owner."""
    def __init__(self, owner: Owner):
        self.owner = owner


    def get_all_tasks(self) -> List[Task]:
        """Get all tasks for the owner."""
        return self.owner.get_all_tasks()


    def get_tasks_for_today(self) -> List[tuple]:
        """Get today's tasks sorted by time, grouped by pet."""
        today = datetime.now().strftime("%A")  # e.g., "Monday"
        pet_tasks = []
        for pet in self.owner.pets:
            todays_tasks = [task for task in pet.get_tasks() if task.frequency.lower() in ("daily", today.lower())]
            for task in todays_tasks:
                pet_tasks.append((pet, task))
        # Sort by time (assume HH:MM 24hr format)
        pet_tasks.sort(key=lambda x: x[1].time)
        return pet_tasks


    def format_schedule(self) -> str:
        """Format and return today's schedule as a string."""
        pet_tasks = self.get_tasks_for_today()
        if not pet_tasks:
            return "No tasks scheduled for today."
        output = ["Today's Schedule:"]
        last_pet = None
        for pet, task in pet_tasks:
            if pet != last_pet:
                output.append(f"\n{pet}:")
                last_pet = pet
            output.append(f"  {task}")
        return "\n".join(output)
