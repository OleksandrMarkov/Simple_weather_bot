import requests, datetime
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
    await message.reply("Hello!")

@dp.message_handler()
async def get_weather(message: types.Message):
    emoji_dict = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F328"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text},&APPID={open_weather_token}&units=metric"
        )

        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

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
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) -\
                            datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await  message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n")
        await  message.reply(f"Weather in city {city}\nTemperature: {cur_weather} °C {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}\nWind: {wind} m/s\n"
              f"Sunrise: {sunrise}\nSunset: {sunset}\nLength of the day: {length_of_the_day}")

    except Exception as ex:
        #print(ex)
        await  message.reply("\U00002620 Wrong input...\U00002620")

if __name__ == "__main__":
    executor.start_polling(dp)