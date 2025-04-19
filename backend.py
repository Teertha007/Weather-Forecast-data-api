from http.client import responses

import requests

API_KEY = "1a59d955b1716443f880d4a44d77b2a4"


def get_data(place,days=1,kind=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responses = requests.get(url)
    data = responses.json()
    filtered_data = data["list"]
    forecast_days = days
    num_values = 8* forecast_days
    filtered_data = filtered_data[:num_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__== "__main__":
    print(get_data(place="Dhaka",days=5, kind="Temperature"))
