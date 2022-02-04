from aiogram import types
from filters import IsGroup

from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_btn import language

from loader import dp

# text = "Assalomu alaykum {} botga xush kelibsiz! \nBu bot orqali siz Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Televizion Texnologiyalari Fakulteti dekaniga o'z Ariza , Shikoyat va Takliflarizni qoldirishiz mumkin!!!"
@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):

	await message.answer("Salom {}! Siz bu botdan guruhda foydalana olmaysiz".format(message.from_user.full_name))
    # await message.answer("O'zingizga qulay tilni tanlang!(🇺🇿/🇷🇺)\n-----\nВыберите удобный Вам язык!(🇺🇿/🇷🇺)", reply_markup=language)
