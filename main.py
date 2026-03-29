# main.py
from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner("Alex")

# Create pets
dog = Pet("Buddy", "dog")
cat = Pet("Whiskers", "cat")

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task1 = Task("Morning walk", "08:00", "daily")
task2 = Task("Feed breakfast", "07:30", "daily")
task3 = Task("Playtime", "18:00", "Saturday")

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Create scheduler and print today's schedule
scheduler = Scheduler(owner)
print(scheduler.format_schedule())
