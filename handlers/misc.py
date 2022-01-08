from aiogram import types

import keyboards as kb
from loader import dp


@dp.callback_query_handler(button=kb.Test.GREETING)
async def on_greeting(query: types.CallbackQuery, button: dict):
    user_name = button['user_name']
    await query.message.answer(f'Рад познакомиться, {user_name}!')
