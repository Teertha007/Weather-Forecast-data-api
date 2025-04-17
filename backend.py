from http.client import responses

import requests

API_KEY = "1a59d955b1716443f880d4a44d77b2a4"


def get_data(place,days=None,kind=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responses = requests.get(url)
    data = responses.json()
    return data

if __name__== "__main__":
    print(get_data(place="Dhaka"))
