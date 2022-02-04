from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from data.config import GROUP_CHAT_ID, BOT_TOKEN

from keyboards.default.menu import tel, menu
from keyboards.inline.inline_btn import language, tekshir
from states.state_data import PersonalData
import re
from aiogram.dispatcher import filters
from aiogram import Bot, types

from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from filters import IsPrivate
from datetime import datetime

# import commands_ru


bot=Bot(token=BOT_TOKEN)


PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




@dp.message_handler(IsPrivate(),text="👨🏼‍💼 Dekan haqida")
async def choose_lang(message:Message):
	await types.ChatActions.upload_photo()
	text = "Televizion texnologiyalar fakulteti dekani t.f.f.d(PhD)-Narzulloyev Oybek Mirzayevich"
	media = types.MediaGroup()
	media.attach_photo(types.InputFile('media\photo\dekan.JPG'), text)
	await message.answer_media_group(media)



@dp.message_handler(IsPrivate(),text="🌐 Tilni o'zgartirish")
async def choose_lang(message:Message):

    await message.answer("O'zingizga qulay tilni tanlang!(🇺🇿/🇷🇺)\n-----\nВыберите удобный Вам язык!(🇺🇿/🇷🇺)",reply_markup=language)
   


@dp.callback_query_handler(text="lang_uz")
async def uz_lang(call: CallbackQuery):
	text = "Bu bot orqali siz Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Televizion Texnologiyalari Fakulteti dekaniga o'z Ariza , Shikoyat va Takliflarizni qoldirishiz mumkin!!!"

	await call.message.delete()
	await call.message.answer(text, reply_markup=menu)
	await call.answer(cache_time=30)
	await call.answer()


@dp.message_handler(IsPrivate(),text="📝 Ariza yozish",state=None)
async def ariza_yozish(message:Message):

    await message.answer("🧑🏻‍🎓 Ism Familiyangiz:",reply_markup=ReplyKeyboardRemove())
    await PersonalData.name.set()



@dp.message_handler(state=PersonalData.name)
async def answer_name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("👨‍👨‍👦‍👦 Guruhingizni kiriting:")
    await PersonalData.group.set()



@dp.message_handler(state=PersonalData.group)
async def answer_group(message:Message,state:FSMContext):
    group = message.text
    await state.update_data(
        {"group":group}
    )
    await message.answer("📱 O'z telefon raqamingizni kiriting, yoki quidagi tugmani bosib o'z kontaktingizni yuboring:",reply_markup=tel,)
    await PersonalData.phone_number.set()
	




@dp.message_handler(state=PersonalData.phone_number, content_types="contact")
async def answer_phone(message:Message, state:FSMContext):
	phone_num = message
	  

	if phone_num.contact:
		# print(phone_num.contact)
		if re.search(PHONE_NUM,phone_num.contact.phone_number) :
        
			await state.update_data(
            	{"phone_number": phone_num.contact.phone_number}
            )
			await message.answer("📅 Ariza matnini kiriting:",reply_markup=ReplyKeyboardRemove())
			await PersonalData.ariza.set()
		
	elif 'text' in phone_num:
		if re.search(PHONE_NUM,phone_num.text):
            
			await state.update_data(
            	{"phone_number": phone_num.text}
            )
			await message.answer("📅 Ariza matnini kiriting:",reply_markup=ReplyKeyboardRemove())
			await PersonalData.ariza.set()
		else:
			await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
			await PersonalData.phone_number.set()



	else:
		await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
		await PersonalData.phone_number.set()





@dp.message_handler(state=PersonalData.ariza)
async def answer_ariza(message:Message,state:FSMContext):
    ariza = message.text
    await state.update_data(
        {"ariza": ariza},
    )




    data = await state.get_data()
    name = data.get("name")
    group = data.get("group")
    phone_number = data.get("phone_number")
    ariza = data.get("ariza")


    today = datetime.today()
    day = f"{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}"

    global msg
    msg = "📌 Yangi ariza! \n\n"
    msg += f"🧑🏻‍🎓 Talaba: {name}\n"
    msg += f"👨‍👨‍👦‍👦 Guruh: {group}\n"
    msg += f"📱 Telefon: {phone_number}\n"
    msg += f"📝 Ariza: {ariza}\n"
    msg += f"⏳ Sana: {day}"

    await message.answer(msg)
    await state.finish()
    await message.answer("Arizani yuborasizmi?", reply_markup=tekshir)




@dp.callback_query_handler(text="send")
async def arizani_yuborish(call: CallbackQuery):
  
    await call.message.delete()
    await bot.send_message(GROUP_CHAT_ID, msg)

    await call.message.answer("✅ Arizangiz yuborildi!",reply_markup=menu)
    await call.answer(cache_time=30)
    await call.answer()



@dp.callback_query_handler(text="wrong")
async def arizani_bekor_qilish(call: CallbackQuery):
  
    await call.message.delete()
    await call.message.answer("❌ Arizangiz bekor qilindi!",reply_markup=menu)
    await call.answer(cache_time=30)
    await call.answer()

