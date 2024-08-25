import streamlit as st
import pandas as pd
import pickle

def show_prediction():
    # Load the trained model
    model = pickle.load(open('model.pkl', 'rb'))

    # Streamlit App
    st.title("Housing Price Prediction")
    st.image("images.jpg")  # Displaying the image

    # Sidebar Inputs
    st.sidebar.title("Housing Data")
    area = st.sidebar.slider("Area (in square feet)", 100, 10000, 7300)
    bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 2)
    bathrooms = st.sidebar.slider("Bathrooms", 1, 5, 1)
    stories = st.sidebar.slider("Stories", 1, 5, 1)
    mainroad = st.sidebar.slider("Main Road (0 = No, 1 = Yes)", 0, 1, 1)
    guestroom = st.sidebar.slider("Guest Room (0 = No, 1 = Yes)", 0, 1, 0)
    basement = st.sidebar.slider("Basement (0 = No, 1 = Yes)", 0, 1, 0)
    hotwaterheating = st.sidebar.slider("Hot Water Heating (0 = No, 1 = Yes)", 0, 1, 0)
    airconditioning = st.sidebar.slider("Air Conditioning (0 = No, 1 = Yes)", 0, 1, 0)
    parking = st.sidebar.slider("Parking", 0, 4, 0)
    prefarea = st.sidebar.slider("Preferred Area (0 = No, 1 = Yes)", 0, 1, 0)
    furnishingstatus = st.sidebar.selectbox("Furnishing Status", ["unfurnished", "semi-furnished", "furnished"])

    # Encoding the furnishing status
    furnishing_mapping = {'unfurnished': 0.0, 'semi-furnished': 0.5, 'furnished': 1.0}
    furnishing_encoded = furnishing_mapping[furnishingstatus]

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'mainroad': [mainroad],
        'guestroom': [guestroom],
        'basement': [basement],
        'hotwaterheating': [hotwaterheating],
        'airconditioning': [airconditioning],
        'parking': [parking],
        'prefarea': [prefarea],
        'furnishingstatus': [furnishing_encoded]
    })

    # Display the input data
    st.write("Housing Data")
    st.write(input_data)

    # Make a prediction
    if st.button("Predict Price"):
        try:
            prediction = model.predict(input_data)[0]
            st.write(f"Predicted House Price: ${prediction:.2f}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
