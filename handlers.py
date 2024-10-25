import os

from aiogram import F, Router, types, flags
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import (
    Message,
    CallbackQuery,
    FSInputFile,
    UserProfilePhotos,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType
    )

import text
import ChatGPT
from states import Reg, get_prompt
#from payments import create, check
from keyboards import (
    start_kb,
    menu_kb,
    payment_kb,
    to_menu_kb,
    practices_lvl_kb,
    lvl_1_kb,
    lvl_2_kb,
    lvl_3_kb,
    lvl_4_kb
    )
import Pictures
 
router = Router()

all_media_dir = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
        ),
    'all_media'
    )

#Команды
#Регистрация пользователя при старте. Данные занести в БД
@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    msg_pic = FSInputFile(path = os.path.join(all_media_dir, Pictures.start_pic))
    await message.answer_photo(
        photo = msg_pic,
        caption = text.greet,
        reply_markup = start_kb,
        parse_mode = 'html'
        )

@router.message(Command('menu'))
async def menu(message: Message, state: FSMContext):
    await state.clear()
    msg_pic = FSInputFile(path = os.path.join(all_media_dir, Pictures.menu_pic))
    await message.answer_photo(
        photo = msg_pic,
        caption = text.menu,
        reply_markup = menu_kb,
        parse_mode = 'html'
        )

#Главное меню
@router.callback_query(F.data == 'menu')
async def menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(show_alert = False)
    await callback.message.delete()
    msg_pic = FSInputFile(
        path = os.path.join(
            all_media_dir,
            Pictures.menu_pic,
            )
        )
    await callback.message.answer_photo(
        photo = msg_pic,
        caption = text.menu,
        reply_markup = menu_kb,
        parse_mode = 'html'
        )

#Практики
@router.callback_query(F.data == 'practices_lvl')
async def practices_lvl(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = text.practices_lvl,
                                  reply_markup = practices_lvl_kb,
                                  parse_mode = 'html'
                                  )

#Практики певрого уровня:
@router.callback_query(F.data == 'lvl_1')
async def lvl_1(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = '<b>🗝  Введение</b>',
                                  reply_markup = lvl_1_kb,
                                  parse_mode = 'html')

#Практики второго уровня:
@router.callback_query(F.data == 'lvl_2')
async def lvl_2(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = '<b>🧘 Пробуждение</b>',
                                  reply_markup = lvl_2_kb,
                                  parse_mode = 'html')

#Практики третьего уровня:
@router.callback_query(F.data == 'lvl_3')
async def lvl_3(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = '<b>🌊 Глубина</b>',
                                  reply_markup = lvl_3_kb,
                                  parse_mode = 'html')

#Практики четвертого уровня:
@router.callback_query(F.data == 'lvl_4')
async def lvl_4(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = '<b>🕳 Расширение</b>',
                                  reply_markup = lvl_4_kb,
                                  parse_mode = 'html')

#Видео
@router.callback_query(F.data == 'videos')
async def videos(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    await callback.message.answer(text = text.videos, parse_mode = 'html')




#Оплата
@router.callback_query(F.data == 'premium')
async def premium(callback: CallbackQuery):
    await callback.answer(show_alert=False)
    await callback.message.delete()
    #payment_url, payment_id = create(PRICE, callback.message.chat.id)
    await callback.message.answer(
        text.premium,
        reply_markup = to_menu_kb,
        parse_mode = 'html'
        )  #f"{payment_url}"


#Чат с ChatGPT
@router.callback_query(F.data == 'support')
async def support(callback: CallbackQuery, state: FSMContext):
    await state.set_state(get_prompt.text_prompt)
    await callback.answer(show_alert = False)
    await callback.message.delete()
    await callback.message.answer(
        text.support,
        parse_mode = 'html'
        )

#Приём промпта
@router.message(get_prompt.text_prompt)
@flags.chat_action('typing')
async def generate_text(message: Message, state: FSMContext):
    await state.set_state(get_prompt.text_prompt)
    prompt = message.text
    gen_message = await message.answer(text.gen_wait)
    res = await ChatGPT.generate_text(prompt)
    if not res:
        return await gen_message.edit_text(
            text.gen_error,
            reply_markup=to_menu_kb
            )
    await gen_message.edit_text(f"{res}\n\nЧтобы завершить чат, отправь /menu")
