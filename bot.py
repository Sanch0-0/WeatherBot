import os
from dotenv import load_dotenv
from telebot import TeleBot
import requests
from datetime import datetime

load_dotenv()

bot = TeleBot(token=os.getenv("TOKEN"))
api_key = os.getenv("API_KEY")


@bot.message_handler(commands=['start'])
def start(message):
    text = (
'''Приветствую!
Данный бот предназначен для получения информации о погоде в нужном вам городе.
Напишите название города для получения информации.'''
            )
    bot.send_message(
        chat_id=message.chat.id,
        text=text
    )


@bot.message_handler(func=lambda message: True)
def find_city(message):
    city = message.text.capitalize()
    url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru")
    data = url.json()

    if data['cod'] == 404:
        reply = "Город не найден"
    elif data['cod'] != 200:
        reply = "Что-то пошло не так"
    else: 
        country = data['sys']['country']
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_feel = data['main']['feels_like']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        reply = (
        f"---------{datetime.now().strftime('%d-%m-%Y - %H:%M')}---------\n"
        f"Страна: {country}\n"
        f"Погода: {weather}\n"
        f"Описание: {description.capitalize()}\n"
        f"Температура: {temp}°C\n"
        f"Ощущается как : {temp_feel}°C\n"
        f"min температура: {min_temp}°C\n"
        f"max температура: {max_temp}°C\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed}м/с\n"
        )
    bot.reply_to(message,reply)

