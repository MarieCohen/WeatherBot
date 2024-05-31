import asyncio

import datetime, requests

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from info import open_weather_token, bot_token_api

dp = Dispatcher()

main_keyboard = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = 'Изменить город', callback_data = 'setlocationkb')]])

@dp.message(CommandStart())
async def get_started(message: types.Message):
    await message.answer(f'Приветствую, {message.from_user.first_name} 🤖\nВведите ваш город, а я подскажу, какая сейчас погода')

@dp.message(Command('setlocation'))
async def set_location_command(message: types.Message):
    await message.answer('Укажите ваш город')

@dp.callback_query(F.data == 'setlocationkb')
async def set_location(callback: CallbackQuery):
    await callback.answer(show_alert = True)
    await callback.message.edit_text('Укажите ваш город')

@dp.message()
async def get_weather(message: types.Message):
    code_to_smile = {
        'clear sky': 'Ясно ☀️',
        'scattered clouds': 'Облачно ☁️',
        'overcast clouds': 'Пасмурно ☁️',
        'shower rain': 'дождь 🌧',
        'drizzle': 'Слабый дождь 💧',
        'mist': 'Туман 🌫',
        'fog': 'Туман 🌫',
        'tornado': 'Торнадо 🌪',
        'thunderstorm': 'Гроза 🌩',
        'thunderstorm with rain': 'Дождь с грозой ⛈',
        'Snow': 'Снег ❄️',
        'Sleet': 'Слякоть 🌨💧',
        'Rain and snow': 'Дождь со снегом 🌨💧',
        'volcano ash': 'Вулканический пепел 🌋🌫',
        } 
    try:
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&appid={open_weather_token}&units=metric")
        data = res.json()

        city = data["name"]
        weather_description = data['weather'][0]['description']

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = weather_description
            
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        if wd == 'облачно' or wd == 'пасмурно':
            day_wish = 'Погода сегодня обманчива, утром и вечером может быть холодно. Стоит выбрать верхнюю одежду, которая не промокнет. Возможны осадки ☔️'
        elif wd == 'гроза' or wd == 'Слякоть' or wd == 'небольшая гроза' or wd == 'сильная гроза' or wd == 'мокрый снег':
            day_wish = 'Прохладно, но не расстраивайтесь! У природы нет плохой погоды 🌤 Возможно, понадобится зонт ☂️'
        elif wd == 'дождь' or wd == 'сильный ливень с моросью' or wd == 'небольшой дождь' or wd == 'умеренный дождь' or wd == 'ливень' or wd == 'сильный ливень' :
            day_wish = 'Ожидаются осадки, а значит на улице значительно похолодает. Перед выходом наденьте куртку или плащ, не забудьте захватить с собой зонт.'
        elif wd == 'дождь со снегом' or wd == 'дождь и снег' or wd == 'сильный дождь' or wd == 'небольшой дождь со снегом' or wd == 'небольшой дождь и снег':
            day_wish = 'Ожидаются осадки, а значит на улице значительно похолодает. Перед выходом наденьте куртку или плащ, не забудьте захватить с собой зонт.'
        elif wd == 'моросящий дождь' or wd == 'слабый моросящий дождь'  or wd == 'сильный моросящий дождь'  or wd == 'мелкий дождь' or wd == 'ледяной дождь':
            day_wish = 'День будет прохладным и с осадками. Дождь несильный, но выходя из дома, берите с собой зонт ☂️'
        elif wd == 'Снег' or wd == 'небольшой снег' or wd == 'сильный снегопад':
            day_wish = 'Морозный день, на улицах может быть скользко, осторожно на дорогах! На выход можно выбрать многослойную одежду. А если повезло остаться дома, лучше согреваться за любимым занятием или с чашкой ароматного напитка.'
        elif wd == 'туман':
            day_wish = 'Сегодня ожидается туман, а значит видимость будет снижаться. Будьте аккуратны на дороге! Так же выходя на прогулку возьмите куртку, возможно похолодание.'
        elif wd == 'чистое небо' or wd == 'ясно':
            day_wish = 'Погода заманивает прогуляться сегодня на свежем воздухе, не отказывайтесь! Осадков не ожидается, в тёплую погоду можно надеть свободную одежду и любимые кроссовки'
    
        await message.answer(f'Привет, {message.from_user.first_name} 👋\n'
                            f'⛅️ Погода в городе {city}\n'
                            f"▫️Сегодня, {datetime.datetime.now().strftime('%d.%m - %H:%M')}▫️\n"
                            f'\nТемпература сейчас: {temp}°C\nОщущается как {feels_like}°C, ☁️ {wd}\n'
                            f'↑Макс {temp_max}°C - ↓Мин {temp_min}°C\n'
                            f'\n💧Влажность: {humidity}%\n🏧Давление: {pressure} мм рт. ст.\n💨Скорость ветра: {wind_speed} м/с\n'
                            f'\n🌇Восход солнца: {sunrise_timestamp}\n🌆Закат солнца: {sunset_timestamp}\n'
                            f'☀️Продолжительность дня: {length_of_the_day}\n'
                            f'\n💭 Совет:\n{day_wish}', reply_markup = main_keyboard)
    except:
        await message.answer(f'Не смог узнать погоду в городе {message.text}...Проверьте ввод!')
        
async def main():
    bot = Bot(bot_token_api)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')