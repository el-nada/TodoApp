import streamlit as st
from database import add_task
from logic import *
from auth.database_auth import get_id

def render():
    
    col1, col2 = st.columns([0.85, 0.15]) 
    with col1:
        st.title(f"Welcome {st.session_state.username}!")
            
    with col2:
        st.write(" ")
        st.write(" ")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

    
    st.title(f"To do list") 

    # Initialize session state flag for success message
    if "task_added" not in st.session_state:
        st.session_state.task_added = False
    if "task_incomplete" not in st.session_state: 
        st.session_state.task_incomplete = False
    
    # Form to capture input (supports Enter key and button click)
    with st.form(key="task_form"):
        task_input = st.text_input("Enter a new task :", key="new_task")
        task_description = st.text_input("Description :", key="new_description")
        due_date = st.date_input("Due date :", value=None)
        task_priority = st.selectbox("Priority :", ["High", "Medium", "Low"], key=f"new_priority",)
        submitted = st.form_submit_button("Add Task")  # Click OR Press Enter
        
        if submitted and task_input and task_description and due_date :
            
            user_id = get_id(st.session_state.username)
            add_task(task_input, task_description, task_priority, user_id, due_date)
            st.session_state.task_added = True
            st.session_state.task_incomplete = False  # Reset the error flag on success
            st.rerun()

        elif (submitted and not task_input) or (submitted and not task_description) or (submitted and not due_date): 
            st.session_state.task_incomplete = True 
            st.rerun()

    search_query = st.text_input("", placeholder="Search by title or description", key='search_input')

    # If a task was added in the previous run, display a success message
    if st.session_state.task_added:
        st.success("Task added!")
        # Reset the flag so the message only shows once
        st.session_state.task_added = False
    if st.session_state.task_incomplete : 
        st.error("Please fill in all the required fields before submitting.")
        
    # Show existing tasks
    show_tasks(
        get_id(st.session_state.username), 
        search_query,
        bool(search_query)
    )
