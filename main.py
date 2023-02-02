from config import open_weather_token
from pprint import pprint
import requests

def get_weather(city, open_weather_token):
    try:
        query_1 = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=25926c8f4fe099bf7856cdedb067e60a"

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city},&APPID={open_weather_token}&units=metric"
        )

        data = r.json()
        pprint(data)

    except Exception as ex:
        print(ex)
        print("Проверьте правильность названия города...")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()