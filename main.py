
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

# Add tasks OUT OF ORDER and with conflicts
dog.add_task(Task("Feed breakfast", "09:00", "daily"))
dog.add_task(Task("Morning walk", "08:00", "daily"))
cat.add_task(Task("Vet visit", "09:00", "weekly"))  # Same time as dog's breakfast
cat.add_task(Task("Playtime", "07:00", "daily"))

# Create scheduler
scheduler = Scheduler(owner)

print("--- Sorted Schedule (All Tasks) ---")
all_tasks = owner.get_all_tasks()
sorted_tasks = scheduler.sort_by_time(all_tasks)
for task in sorted_tasks:
	print(f"{task}")

print("\n--- Incomplete Tasks Only ---")
incomplete = scheduler.filter_by_status(all_tasks, completed=False)
for task in incomplete:
	print(f"{task}")

print("\n--- Conflict Warnings ---")
conflicts = scheduler.detect_conflicts(all_tasks)
if conflicts:
	for warning in conflicts:
		print(warning)
else:
	print("No conflicts detected.")

# Demonstrate recurring task logic
print("\n--- Marking a daily task complete (should add a new one) ---")
task_to_complete = dog.get_tasks()[0]  # Feed breakfast
print(f"Before: {len(dog.get_tasks())} tasks for {dog.name}")
scheduler.mark_task_complete(task_to_complete, dog)
print(f"After: {len(dog.get_tasks())} tasks for {dog.name}")
print("Newest task:", dog.get_tasks()[-1])
