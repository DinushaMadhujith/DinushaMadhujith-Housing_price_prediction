import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_explore():
    # Load the dataset
    housing_data = pd.read_csv('Housing.csv')

    st.title("Housing Data Exploration")

    # Show the dataset
    st.subheader("Dataset Overview")
    st.write(housing_data.head())

    # Show basic statistics
    st.subheader("Dataset Statistics")
    st.write(housing_data.describe())

    # Data Exploration through Visualization
    st.sidebar.title("Visualization Options")
    visualization_type = st.sidebar.selectbox("Choose Visualization Type", ["Distribution Plot", "Box Plot", "Correlation Heatmap"])

    # Distribution Plot
    if visualization_type == "Distribution Plot":
        column = st.sidebar.selectbox("Select Column", housing_data.columns)
        plt.figure(figsize=(10, 6))
        sns.histplot(housing_data[column], kde=True)
        plt.title(f"Distribution Plot of {column}")
        st.pyplot(plt)

    # Box Plot
    elif visualization_type == "Box Plot":
        column = st.sidebar.selectbox("Select Column", housing_data.columns)
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=housing_data, x=column)
        plt.title(f"Box Plot of {column}")
        st.pyplot(plt)

    # Correlation Heatmap
    elif visualization_type == "Correlation Heatmap":
        cor_matrix = housing_data.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        st.pyplot(plt)

    # Data Filtering
    st.sidebar.title("Data Filtering")
    min_area = st.sidebar.slider("Minimum Area", int(housing_data['area'].min()), int(housing_data['area'].max()), int(housing_data['area'].min()))
    max_area = st.sidebar.slider("Maximum Area", int(housing_data['area'].min()), int(housing_data['area'].max()), int(housing_data['area'].max()))

    filtered_data = housing_data[(housing_data['area'] >= min_area) & (housing_data['area'] <= max_area)]
    st.subheader(f"Filtered Data (Area between {min_area} and {max_area} sqft)")
    st.write(filtered_data)

    # Optional: Save filtered data as CSV
    if st.sidebar.button("Download Filtered Data"):
        filtered_data.to_csv("filtered_housing_data.csv", index=False)
        st.sidebar.success("Filtered data saved as 'filtered_housing_data.csv'")
