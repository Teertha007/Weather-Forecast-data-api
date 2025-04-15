import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Enter the name of the place:")
days = st.slider("Forecast Days",min_value=1,max_value =5,
                 help="Fuck off.Try to open your eye and see")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for next {days} in {place}")
