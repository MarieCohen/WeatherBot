from aiogram.types import(
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton, 
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)


start = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть портал 🕳️',
                          callback_data = 'menu')]])


menu = [
    [InlineKeyboardButton(text = '💬 Чат с ChatGPT', callback_data = 'support')],
    [InlineKeyboardButton(text = '🧘 Практики', callback_data = 'practices_lvl'),
    InlineKeyboardButton(text = '🗝 Видео', callback_data = 'videos')],
    [InlineKeyboardButton(text = '🌟 Premium подписка', callback_data = 'premium')],
    [InlineKeyboardButton(text = '❓ ЧаВо', url = 'https://telegra.ph/FAQ-dlya-bota-SOULnear-10-22')]
]
menu = InlineKeyboardMarkup(inline_keyboard = menu)


profile = [
    [InlineKeyboardButton(text = '📷 Фото', callback_data = 'set_photo'),
    InlineKeyboardButton(text = '🖋 Имя', callback_data = 'set_name')],
    [InlineKeyboardButton(text = '👫 Пол', callback_data = 'set_gender'),
    InlineKeyboardButton(text = '👥 Возраст', callback_data = 'set_age')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]
]
profile = InlineKeyboardMarkup(inline_keyboard = profile)



#Выбор периода подписки
premium = [
    [InlineKeyboardButton(text = '1 месяц/499 ₽', callback_data = 'pay_1')],
    [InlineKeyboardButton(text = '3 месяцa/1119 ₽', callback_data = 'pay_2')],
    [InlineKeyboardButton(text = '12 месяцев/3999 ₽', callback_data = 'pay_3')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]
]
premium = InlineKeyboardMarkup(inline_keyboard = premium)

#Подписка на 1 мес
pay_1 = [
    [InlineKeyboardButton(text = '💳 Оплатить 499,00 ₽', url = 'https://t.me/SoulnearBot')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'premium')]
]
pay_1 = InlineKeyboardMarkup(inline_keyboard = pay_1)

#Подписка на 3 мес
pay_2 = [
    [InlineKeyboardButton(text = '💳 Оплатить 1119,00 ₽', url = 'https://t.me/SoulnearBot')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'premium')]
]
pay_2 = InlineKeyboardMarkup(inline_keyboard = pay_2)

#Подписка на 12 мес
pay_3 = [
    [InlineKeyboardButton(text = '💳 Оплатить 3999,00 ₽', url = 'https://t.me/SoulnearBot')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'premium')]
]
pay_3 = InlineKeyboardMarkup(inline_keyboard = pay_3)



#Возвратиться в меню
to_menu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]])



#Практики делятся на 4 уровня: Введение, Пробуждение, Глубина, Расширение.
#Выбор уровня:
practices_lvl = [
    [InlineKeyboardButton(text = '🗝  Введение', callback_data = 'lvl_1')],
    [InlineKeyboardButton(text = '🧘 Пробуждение', callback_data = 'lvl_2')],
    [InlineKeyboardButton(text = '🌊 Глубина', callback_data = 'lvl_3')],
    [InlineKeyboardButton(text = '🕳 Расширение', callback_data = 'lvl_4')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]
]
practices_lvl = InlineKeyboardMarkup(inline_keyboard = practices_lvl)

#Практики первого уровня:
lvl_1 = [
    [InlineKeyboardButton(text = 'Погружение в медитацию',
                          url = 'https://telegra.ph/Pogruzhenie-v-meditaciyu-podgotovka-tela-nastrojka-ehnergii-i-sekrety-uspeshnoj-praktiki-10-21')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_1 = InlineKeyboardMarkup(inline_keyboard = lvl_1)

#Практики второго уровня:
lvl_2 = [
    [InlineKeyboardButton(text = 'Осознанное дыхание',
                          url = 'https://telegra.ph/Probuzhdenie--praktiki-do-15-minut-10-22'),
    InlineKeyboardButton(text = 'Осознанная ходьба',
                         url = 'https://telegra.ph/Praktika-Osoznannaya-hodba-10-22')],
    [InlineKeyboardButton(text = 'Медитация #1',
                          url= 'https://telegra.ph/Praktika-Bazovaya-meditaciya-na-rasslablenie-10-22'),
    InlineKeyboardButton(text = 'Медитация #2',
                         url = 'https://telegra.ph/Praktika-Meditaciya-na-vizualizaciyu-10-22')],
    [InlineKeyboardButton(text = 'Медитация #3',
                          url = 'https://telegra.ph/Praktika-Meditaciya-na-osoznanie-tela-10-22')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_2 = InlineKeyboardMarkup(inline_keyboard = lvl_2)

#Практики третьего уровня:
lvl_3 = [
    [InlineKeyboardButton(text = 'Медитация Ошо',
                          url = 'https://telegra.ph/Dinamicheskaya-meditaciya-Osho-10-21'),
    InlineKeyboardButton(text = 'Медитация #2',
                         url = 'https://telegra.ph/Praktika-Meditaciya-na-nablyudenie-za-myslyami-10-22')],
    [InlineKeyboardButton(text = '«Дыхательная»',
                          url= 'https://telegra.ph/Praktika-EHmocionalnoe-osvobozhdenie-cherez-dyhanie-10-22'),
    InlineKeyboardButton(text = 'Випассана',
                         url = 'https://telegra.ph/Vipassana-Pogruzhenie-v-nablyudenie-i-osoznannost-10-22-2')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_3 = InlineKeyboardMarkup(inline_keyboard = lvl_3)

#Практики четвертого уровня:
lvl_4 = [
    [InlineKeyboardButton(text = 'Гудящая медитация',
                          url = 'https://telegra.ph/Gudyashchaya-meditaciya--dinamicheskaya-praktika-kotoraya-vklyuchaet-zvukovye-vibracii-i-medlennye-dvizheniya-ruk-10-22')],
    [InlineKeyboardButton(text = '«Внутренняя тишина»',
                         url = 'https://telegra.ph/Meditaciya-na-vnutrennyuyu-tishinu-10-22')],
    [InlineKeyboardButton(text = 'Медитация #2',
                          url = 'https://telegra.ph/Praktika-EHnergeticheskaya-meditaciya-10-22')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_4 = InlineKeyboardMarkup(inline_keyboard = lvl_4)
