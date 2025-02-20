import streamlit as st
from database import *

# Function to display tasks
def show_tasks(user_id):
    tasks = get_tasks(user_id)
    if tasks:
        for task_id, task, description, priority, status, date in tasks:
            # Initialize session state for change tracking
            if f"original_{task_id}" not in st.session_state:
                st.session_state[f"original_{task_id}"] = {
                    "status": status,
                    "priority": priority,
                    "date": date
                }

            
            with st.expander(task +": "+status+" due : "+date):
                st.write(f"**Description:** {description}")

                with st.form(key=f"task_form_{task_id}"):
                    # Get current values from session state or database
                    current_date = st.session_state[f"original_{task_id}"]["date"]
                    current_status = st.session_state[f"original_{task_id}"]["status"]
                    current_priority = st.session_state[f"original_{task_id}"]["priority"]

                    # Input fields
                    new_date = st.date_input("Due date:", value=current_date)
                    new_status = st.selectbox(
                        "Status",
                        ["Pending", "Completed"],
                        index=0 if current_status == "Pending" else 1,
                        key=f"status_{task_id}"
                    )
                    new_priority = st.selectbox(
                        "Priority:", 
                        ["High", "Medium", "Low"], 
                        index=["High", "Medium", "Low"].index(current_priority),
                        key=f"priority_{task_id}"
                    )

                    # Check for changes
                    changes_detected = (
                        (new_status != current_status) or
                        (new_priority != current_priority) or
                        (new_date != current_date)
                    )

                    # Submit button with conditional logic
                    if st.form_submit_button("Save Changes", disabled=not changes_detected):
                        if changes_detected:
                            # Update database
                            update_status(task_id, new_status, user_id)
                            update_priority(task_id, new_priority, user_id)
                            update_date(task_id, new_date.isoformat(), user_id)
                            
                            # Update original values in session state
                            st.session_state[f"original_{task_id}"] = {
                                "status": new_status,
                                "priority": new_priority,
                                "date": new_date
                            }
                            st.rerun()
                        else:
                            st.warning("No changes detected")

                if st.button("Delete", key=f"del_{task_id}"):
                    delete_task(task_id, user_id)
                    del st.session_state[f"original_{task_id}"]
                    st.rerun()
    else:
        st.info("No tasks yet. Add a new task above!")



