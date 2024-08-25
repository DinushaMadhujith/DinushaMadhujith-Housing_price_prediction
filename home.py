import streamlit as st
from PIL import Image

# Display the main title and subtitle
def show_home():
    st.title("Welcome to the House Price Prediction App 🏠")
    st.markdown("""
<div style="text-align: justify;">
Use this app to predict house prices and explore housing data.

This interactive application is designed to assist you in predicting house prices based on various features like area, number of bedrooms, and furnishing status. Whether you’re buying or selling a property, this app provides accurate price predictions and valuable insights. By inputting details such as the number of rooms, square footage, and other specifications, you can estimate the selling price with our advanced machine learning model. Additionally, explore trends and patterns in housing data, such as average prices for different locations and property types, and discover the distribution of house prices across various features. This app is an essential tool for home buyers, sellers, and real estate enthusiasts alike, offering a comprehensive view of the housing market.
</div>
""", unsafe_allow_html=True)

# Add an image
    image = Image.open('images.jpeg')
    st.image(image, caption="Get insights into house prices with our predictive model", use_column_width=True)

# Footer or additional information
    st.write("""
---
Created by [S.H.D.Madhujith](https://github.com/your-github-profile).
For more information, visit the [GitHub repository](https://github.com/your-repository).
""")

    if __name__ == "__main__":
        main()
