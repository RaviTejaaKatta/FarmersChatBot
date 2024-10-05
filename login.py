import streamlit as st
import subprocess

# Function to validate user credentials
def authenticate(username, password):
    # Placeholder authentication logic
    # In a real app, you would check these credentials against a database
    if username == "Ravi" and password == "123":
        return True
    else:
        return False

# Streamlit app layout
st.title("Farming Chatbot Login")

# Create input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")
st_app_path = "C:\\Users\\katta\\VS CODE\\LLMmodel\\LLM\\app.py"

# Create a login button
if st.button("Login"):
    if authenticate(username, password):
        st.success(f"Welcome {username}!")
        # You can add code here to display the chatbot interface
        st.write("You can now interact with the farming chatbot.")
        subprocess.Popen(["streamlit", "run", st_app_path])
    else:
        st.error("Invalid username or password. Please try again.")

# Note: In a real-world scenario, you'd want to hash passwords and use a secure method for authentication.
