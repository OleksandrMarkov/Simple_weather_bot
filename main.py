from config import open_weather_token
from pprint import pprint
import requests, datetime

def get_weather(city, open_weather_token):

    emoji_dict = {
        "Clear" : "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F328"
    }

    try:
        query_1 = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=25926c8f4fe099bf7856cdedb067e60a"

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city},&APPID={open_weather_token}&units=metric"
        )

        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data ["main"]["temp"]

        weather_desc = data["weather"][0]["main"]

        if weather_desc in emoji_dict:
            wd = emoji_dict[weather_desc]
        else:
            wd = "Look at window!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"] - data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n")
        print(f"Weather in city {city}\nTemperature: {cur_weather} °C {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}\nWind: {wind} m/s\n"
              f"Sunrise: {sunrise}\nSunset: {sunset}\nLength of the day: {length_of_the_day}")

    except Exception as ex:
        print(ex)
        print("Проверьте правильность названия города...")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()