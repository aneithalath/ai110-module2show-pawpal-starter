## Final UML Diagram

```mermaid
classDiagram
    class Task {
        - description: str
        - time: str
        - frequency: str
        - completed: bool
        + mark_complete()
        + __str__()
    }
    class Pet {
        - name: str
        - species: str
        - tasks: List[Task]
        + add_task(task)
        + get_tasks()
        + __str__()
    }
    class Owner {
        - name: str
        - pets: List[Pet]
        + add_pet(pet)
        + get_all_tasks()
        + __str__()
    }
    class Scheduler {
        - owner: Owner
        + sort_by_time(tasks)
        + filter_by_status(tasks, completed)
        + filter_by_pet(pet_name)
        + detect_conflicts(tasks)
        + mark_task_complete(task, pet)
        + get_all_tasks()
        + get_tasks_for_today()
        + format_schedule()
    }
    Owner "1" -- "*" Pet : has
    Pet "1" -- "*" Task : has
    Scheduler "1" -- "1" Owner : uses
```

---

**How to render/export this diagram:**
- Go to https://mermaid.live
- Paste the code block above
- Click 'Export' > 'Download as PNG'
- Save as uml_final.png in your project folder
