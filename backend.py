import requests

API_KEY = 


def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responses = requests.get(url)
    data = responses.json()
    filtered_data = data["list"]
    forecast_days = days
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    dates = [dict["dt_txt"] for dict in filtered_data]

    if kind == "Temperature":
        filtered_temp = [dict["main"]["temp"] for dict in filtered_data]
        filtered_temp_data = [round(temp - 273.15, 2) for temp in filtered_temp]
        return filtered_temp_data,dates
    elif kind == "Sky":
        filtered_sky_data = [dict["weather"][0]["main"] for dict in filtered_data]
        return filtered_sky_data, dates


if __name__ == "__main__":
    print(get_data(place="Dhaka", days=5, kind="Temperature"))
