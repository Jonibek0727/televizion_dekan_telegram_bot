from aiogram import types
from filters import IsPrivate

from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_btn import language

from loader import dp

text = "Assalomu alaykum {} botga xush kelibsiz! \n-----\nПривет {}, добро пожаловать в бот!"
@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):

	await message.answer(text.format(message.from_user.full_name,message.from_user.full_name))
	await message.answer("O'zingizga qulay tilni tanlang!(🇺🇿/🇷🇺)\n-----\nВыберите удобный Вам язык!(🇺🇿/🇷🇺)", reply_markup=language)



    


 