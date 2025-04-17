import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Weather Forecast for the Next Days")
place = st.text_input("Enter the name of the place:")
days = st.slider("Forecast Days",min_value=1,max_value =5,
                 help="Fuck off.Try to open your eye and see")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} of next {days} in {place}")

def get_data(days):
    dates = ["2024-09-10","2027-10-15","2032-05-08"]
    temperatures = [10,11,16]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d,t =get_data(days)

figure = px.line(x=d,y=t,labels={"x":"Date","y":"Temperature(C)"})
st.plotly_chart(figure)
