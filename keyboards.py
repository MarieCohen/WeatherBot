from aiogram.types import(
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton, 
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)


start_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Открыть портал 🕳️',
                          callback_data = 'menu')]])


menu_kb = [
    [InlineKeyboardButton(text = '💬 Чат с ChatGPT', callback_data = 'support')],
    [InlineKeyboardButton(text = '🧘 Практики', callback_data = 'practices_lvl'),
    InlineKeyboardButton(text = '🗝 Видео', callback_data = 'videos')],
    [InlineKeyboardButton(text = '🌟 Premium подписка', callback_data = 'premium')],
    [InlineKeyboardButton(text = '❓ ЧаВо', url = 'https://telegra.ph/FAQ-dlya-bota-SOULnear-10-22')]
]
menu_kb = InlineKeyboardMarkup(inline_keyboard = menu_kb)


profile_kb = [
    [InlineKeyboardButton(text = '📷 Фото', callback_data = 'set_photo'),
    InlineKeyboardButton(text = '🖋 Имя', callback_data = 'set_name')],
    [InlineKeyboardButton(text = '👫 Пол', callback_data = 'set_gender'),
    InlineKeyboardButton(text = '👥 Возраст', callback_data = 'set_age')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]
]
profile_kb = InlineKeyboardMarkup(inline_keyboard = profile_kb)


payment_kb = [
    [InlineKeyboardButton(text = '💳 Оплатить 190,00 ₽', callback_data = 'buy'),
    InlineKeyboardButton(text = '🔍 Проверить оплату', callback_data = 'chek_payment')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')
    ]
]
payment_kb = InlineKeyboardMarkup(inline_keyboard = payment_kb)


to_menu_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]])




#Практики делятся на 4 уровня: Введение, Пробуждение, Глубина, Расширение.
#Выбор уровня:
practices_lvl_kb = [
    [InlineKeyboardButton(text = '🗝  Введение', callback_data = 'lvl_1')],
    [InlineKeyboardButton(text = '🧘 Пробуждение', callback_data = 'lvl_2')],
    [InlineKeyboardButton(text = '🌊 Глубина', callback_data = 'lvl_3')],
    [InlineKeyboardButton(text = '🕳 Расширение', callback_data = 'lvl_4')],
    [InlineKeyboardButton(text = '↩️ Назад', callback_data = 'menu')]
]
practices_lvl_kb = InlineKeyboardMarkup(inline_keyboard = practices_lvl_kb)

#Практики первого уровня:
lvl_1_kb = [
    [InlineKeyboardButton(text = 'Погружение в медитацию',
                          url = 'https://telegra.ph/Pogruzhenie-v-meditaciyu-podgotovka-tela-nastrojka-ehnergii-i-sekrety-uspeshnoj-praktiki-10-21')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_1_kb = InlineKeyboardMarkup(inline_keyboard = lvl_1_kb)

#Практики второго уровня:
lvl_2_kb = [
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
lvl_2_kb = InlineKeyboardMarkup(inline_keyboard = lvl_2_kb)

#Практики третьего уровня:
lvl_3_kb = [
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
lvl_3_kb = InlineKeyboardMarkup(inline_keyboard = lvl_3_kb)

#Практики четвертого уровня:
lvl_4_kb = [
    [InlineKeyboardButton(text = 'Гудящая медитация',
                          url = 'https://telegra.ph/Gudyashchaya-meditaciya--dinamicheskaya-praktika-kotoraya-vklyuchaet-zvukovye-vibracii-i-medlennye-dvizheniya-ruk-10-22')],
    [InlineKeyboardButton(text = '«Внутренняя тишина»',
                         url = 'https://telegra.ph/Meditaciya-na-vnutrennyuyu-tishinu-10-22')],
    [InlineKeyboardButton(text = 'Медитация #2',
                          url = 'https://telegra.ph/Praktika-EHnergeticheskaya-meditaciya-10-22')],
    [InlineKeyboardButton(text = '↩️ Назад',
                          callback_data = 'practices_lvl')]
]
lvl_4_kb = InlineKeyboardMarkup(inline_keyboard = lvl_4_kb)
