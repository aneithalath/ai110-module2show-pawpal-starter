# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

In my initial UML design, I included four main classes: Owner, Pet, Task, and Planner. The Owner class was responsible for holding user information and a list of their pets. The Pet class stored details about each pet. The Task class represented individual care tasks, and the Planner class managed the scheduling of tasks. Initially, the relationships were simple: Owner had pets, Planner had tasks, and there was no explicit link between tasks and pets or between Planner and Owner.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I realized the need for stronger relationships between the classes. I updated the Task class to reference the specific Pet it belongs to, and I made the Planner class aware of both the Owner and their Pets, not just a list of tasks. I also added methods for managing pets in Owner and for managing tasks in Planner. These changes were made to better support multi-pet owners and to ensure the scheduling logic could access all the information it needs to generate accurate plans.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers time (HH:MM), task completion status, and recurrence as primary constraints. Priority is implicit in the order of tasks, and the system also checks for conflicts when two tasks are scheduled at the same time. I decided that time and conflict detection were most important for a pet care app, as users need to avoid overlapping care tasks and ensure all pets' needs are met on schedule. Simplicity and clarity for the user were prioritized over more complex constraints like preferences or durations.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff is that the scheduler only detects exact time conflicts, not overlapping durations or more nuanced scheduling issues. This makes the logic much simpler and easier for users to understand, which is appropriate for a home pet care context where tasks are usually discrete and not long-running. It avoids overwhelming users with unnecessary complexity and keeps the interface user-friendly.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI tools extensively for brainstorming class designs, generating UML diagrams, and iteratively improving both backend logic and the Streamlit UI. AI was also helpful for writing and refining test cases, as well as for documentation and code review. The most helpful prompts were those that asked for concrete examples, edge case handling, and step-by-step code improvements.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

At one point, the AI suggested a more complex conflict detection algorithm that considered overlapping durations, but I chose not to implement it to keep the app simple. I evaluated the suggestion by considering the needs of typical users and the scope of the project, deciding that exact time conflicts were sufficient. I also verified AI-generated code by running tests and checking that the UI remained clear and intuitive.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task sorting, recurrence handling, conflict detection, and filtering by pet and status. These tests were important to ensure that the scheduler behaves predictably and robustly, especially when users add tasks out of order or mark them as complete. Testing also helped catch edge cases, such as tasks with the same time or recurring tasks for multiple pets.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am highly confident that the scheduler works as intended for the main use cases, thanks to comprehensive tests and manual UI checks. If I had more time, I would test edge cases like tasks scheduled at midnight, handling of daylight saving time changes, and very large numbers of tasks or pets to ensure scalability and robustness.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with the seamless integration between the backend scheduling logic and the Streamlit UI, which provides a user-friendly and interactive experience. The clear documentation and comprehensive test suite also contribute to the overall quality of the project.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would consider adding support for overlapping task durations, notifications or reminders, and a more sophisticated priority system. I would also improve the UI to allow for easier editing and rescheduling of tasks.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important takeaway is that iterative design, with frequent testing and feedback (including from AI), leads to a more robust and user-friendly system. Working with AI is most effective when you combine its suggestions with your own judgment and domain knowledge.
