import plotly.express as px
import streamlit as st
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Enter the name of the place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Fuck off.Try to open your eye and see")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} of next {days} in {place}")

data = get_data(place,days,option)

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure)
