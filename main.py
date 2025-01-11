import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
projects_data = {
    "Project Name": ["Project A", "Project B", "Project C", "Project D", "Project E", "Project F"],
    "Completion (%)": [75, 50, 20, 90, 10, 40],
    "Deadline": ["2025-02-01", "2025-03-15", "2025-04-10", "2025-01-31", "2025-05-20", "2025-06-30"]
}

employees_data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Role": ["Developer", "Designer", "Manager", "Tester"],
    "Assigned Projects": [["Project A", "Project C"], ["Project B"], ["Project A", "Project D"], ["Project F"]],
    "Contribution (%)": [40, 20, 25, 15]
}

# Convert data into DataFrames
projects_df = pd.DataFrame(projects_data)
employees_df = pd.DataFrame(employees_data)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Projects Dashboard", "Employees"])

# Projects Dashboard Page
if page == "Projects Dashboard":
    st.title("Projects Progress Dashboard")
    
    # Display project table
    st.subheader("Project Details")
    st.table(projects_df)
    
    # Project Progress Visualization
    st.subheader("Completion Progress")
    fig, ax = plt.subplots()
    ax.bar(projects_df["Project Name"], projects_df["Completion (%)"], color="skyblue")
    ax.set_ylabel("Completion (%)")
    ax.set_title("Project Progress")
    st.pyplot(fig)
    
    # Filter Projects by Completion
    st.subheader("Filter Projects by Completion")
    threshold = st.slider("Minimum Completion (%)", 0, 100, 50)
    filtered_projects = projects_df[projects_df["Completion (%)"] >= threshold]
    st.table(filtered_projects)

# Employees Page
elif page == "Employees":
    st.title("Employees Overview")
    
    # Display employee table
    st.subheader("Employee Details")
    st.table(employees_df)
    
    # Employee Contribution Details
    st.subheader("Employee Contribution")
    employee_name = st.selectbox("Select Employee", employees_df["Name"])
    employee_data = employees_df[employees_df["Name"] == employee_name].iloc[0]
    
    st.write(f"**Role:** {employee_data['Role']}")
    st.write(f"**Assigned Projects:** {', '.join(employee_data['Assigned Projects'])}")
    st.write(f"**Contribution (%):** {employee_data['Contribution (%)']}")
