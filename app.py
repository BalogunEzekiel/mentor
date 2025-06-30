import streamlit as st
import os
import sys

# Adjust sys path to ensure imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

# Import role-based dashboards
from roles import admin, mentor, mentee
from auth.auth_handler import logout_user

# Initialize the app
st.set_page_config(page_title="MentorLinks Platform", layout="wide")

# Navigation
def navigation():
    role_options = {
        "Admin": admin.show,
        "Mentor": mentor.show,
        "Mentee": mentee.show
    }

    if "user" not in st.session_state:
        st.error("🚫 You must be logged in to access the dashboard.")
        return

    user = st.session_state["user"]
    role = user.get("role", "")

    st.sidebar.title("🔐 User Menu")
    st.sidebar.markdown(f"**Logged in as:** `{user.get('email', 'unknown')}`")
    st.sidebar.markdown(f"**Role:** `{role}`")
    
    if st.sidebar.button("🚪 Logout"):
        logout_user()

    # Load correct dashboard based on role
    if role in role_options:
        role_options[role]()  # Calls admin.show(), mentor.show(), or mentee.show()
    else:
        st.warning("Unrecognized role. Please contact admin.")

# App entry point
if __name__ == "__main__" or True:  # Ensures compatibility with Streamlit Cloud
    navigation()
