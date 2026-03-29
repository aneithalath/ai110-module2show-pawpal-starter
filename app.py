import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# --- Session State Setup ---
# Use session_state to persist the Owner instance across reruns
if "owner" not in st.session_state:
    st.session_state["owner"] = Owner("User")  # You can prompt for a name if desired

owner = st.session_state["owner"]

st.title("🐾 PawPal+ Pet Care Scheduler")

# --- Add a Pet Section ---
st.header("Add a Pet")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet Name")
    pet_species = st.text_input("Species (e.g., dog, cat, bird)")
    add_pet_submitted = st.form_submit_button("Add Pet")
    if add_pet_submitted:
        if pet_name and pet_species:
            new_pet = Pet(pet_name, pet_species)
            owner.add_pet(new_pet)
            st.success(f"Added pet: {pet_name} ({pet_species})")
        else:
            st.warning("Please enter both a pet name and species.")

# --- Add a Task Section ---
st.header("Add a Task")
if owner.pets:
    pet_names = [f"{pet.name} ({pet.species})" for pet in owner.pets]
    pet_lookup = {f"{pet.name} ({pet.species})": pet for pet in owner.pets}
    with st.form("add_task_form"):
        selected_pet_name = st.selectbox("Select Pet", pet_names)
        task_desc = st.text_input("Task Description")
        task_time = st.text_input("Time (e.g., 08:00)")
        task_freq = st.text_input("Frequency (e.g., daily, Monday)")
        add_task_submitted = st.form_submit_button("Add Task")
        if add_task_submitted:
            if selected_pet_name and task_desc and task_time and task_freq:
                task = Task(task_desc, task_time, task_freq)
                pet = pet_lookup[selected_pet_name]
                pet.add_task(task)
                st.success(f"Added task to {selected_pet_name}: {task_desc} at {task_time} ({task_freq})")
            else:
                st.warning("Please fill in all task fields.")
else:
    st.info("Add a pet before adding tasks.")

# --- Display Schedule Section ---
st.header("Today's Schedule")
scheduler = Scheduler(owner)
schedule_str = scheduler.format_schedule()
st.markdown(f"```\n{schedule_str}\n```")

# --- Optional: Show all pets and their tasks ---
with st.expander("Show all pets and their tasks"):
    if owner.pets:
        for pet in owner.pets:
            st.subheader(f"{pet.name} ({pet.species})")
            if pet.tasks:
                for task in pet.tasks:
                    st.write(str(task))
            else:
                st.write("No tasks for this pet yet.")
    else:
        st.write("No pets added yet.")

# Note: st.session_state persists the Owner and all pets/tasks across reruns,
# so user data is not lost when interacting with the app.