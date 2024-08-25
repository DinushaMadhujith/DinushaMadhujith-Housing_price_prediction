import streamlit as st
from home import show_home
from prediction import show_prediction
from explore import show_explore

# Set page configuration
st.set_page_config(
    page_title="House Price Prediction App",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Predict", "Explore"])

# Show the selected page
if page == "Home":
    show_home()
elif page == "Predict":
    show_prediction()
elif page == "Explore":
    show_explore()
