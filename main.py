import plotly.express as px
import streamlit as st
from backend import get_data
#from main import image_path

st.title("Weather Forecast for the Next Days")
place = st.text_input("Enter the name of the place:")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        # Get data directly (temperatures or sky conditions)
        data,dates = get_data(place, days, option)

        if option == "Temperature":
            figure = px.line(
                x=dates,
                y=data,
                labels={"x": "Date", "y": "Temperature (°C)"}
            )
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png","Snow": "images/snow.png"}
            image_path = [ images [condition] for condition in data]
            print(data)
            st.image(image_path,width=115, caption=data)
    except Exception as e:
        st.error(f"Error: {str(e)}")