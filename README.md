# DinushaMadhujith-Housing_price_prediction
🏠 House Price Prediction App
This is a Streamlit web application that predicts house prices based on various input features. The app allows users to explore housing data, visualize relationships between different features, and use a machine learning model to predict house prices.

🌟 Overview
The House Price Prediction app is designed to predict house prices based on key features such as area, bedrooms, bathrooms, and more. Users can explore the dataset, visualize trends, and filter data, making it a powerful tool for understanding housing prices.

🎥 Demo
Demo: Link to Streamlit App https://dinushamadhujith-housingpriceprediction-ggpjs2uygutlrtpeyy9rov.streamlit.app/

GitHub Repository: House Price Prediction App (https://github.com/DinushaMadhujith/DinushaMadhujith-Housing_price_prediction)


🚀 Features

Home Page: A landing page introducing the app and guiding users to explore features or make predictions.

Data Exploration: Visualize and explore the housing dataset with various plotting options, including distribution plots, box plots, and correlation heatmaps.

Prediction: Use a pre-trained machine learning model to predict house prices based on user input.

Data Filtering: Filter the dataset based on area and other features, and download the filtered data as a CSV file.

🛠️ Installation

Python package installer


🧠 How It Works

1. Data Exploration
   
The explore.py script loads the dataset (Housing.csv) and provides options for visualizing the data using Seaborn and Matplotlib. Users can select different types of plots (distribution plots, box plots, and correlation heatmaps) and filter data based on area.

3. Prediction
   
The prediction.py script loads a pre-trained machine learning model (model.pkl) using pickle.
User inputs are gathered via the sidebar (e.g., area, bedrooms, bathrooms) and passed to the model for prediction.
The predicted house price is displayed on the page.

5. Navigation
   
The main.py script controls the app's navigation between the Home, Predict, and Explore pages using Streamlit’s selectbox in the sidebar. Pages are dynamically loaded by calling functions from home.py, explore.py, and prediction.py.


🔧 Technologies Used

Python: Programming language for building the app.

Streamlit: Framework for building interactive web apps in Python.

Pandas: Library for data manipulation and analysis.

Seaborn & Matplotlib: Libraries for data visualization.

Scikit-learn: Library for machine learning.

Pickle: Python module for serializing the machine learning model.
