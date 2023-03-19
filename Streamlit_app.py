import streamlit as st

# Define function for each page
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2")

def page3():
    st.title("Page 3")
    st.write("Welcome to Page 3")

# Create navigation sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1", "Page 2", "Page 3"])

# Display the appropriate page based on user selection
if page == "Page 1":
    page1()
elif page == "Page 2":
    page2()
elif page == "Page 3":
    page3()
