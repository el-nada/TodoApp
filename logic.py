import streamlit as st

from database import *

# Function to display tasks
def show_tasks():
    tasks = get_tasks()
    if tasks:
        for task_id, task, description, status in tasks:
            # Create an expander section for each task
            col1, col2 = st.columns([12, 1])
            with col1  : 
                with st.expander(task):
                    # Display task description
                    st.write(f"**Description:** {description}")

                    # Use a container for alignment
                    with st.container():
                            # Status selection for the task
                            new_status = st.selectbox(
                                "Status",
                                ["Pending", "Completed"],
                                key=f"status_{task_id}",
                                index=0 if status == "Pending" else 1
                            )
                            if new_status != status:
                                update_status(task_id, new_status)
                                st.rerun()

                with col2:
                    # Delete button for the task
                    if st.button("❌", key=f"del_{task_id}"):
                        delete_task(task_id)
                        st.rerun()  # Rerun to reflect changes  
    else:
        st.info("No tasks yet. Add a new task above!")



