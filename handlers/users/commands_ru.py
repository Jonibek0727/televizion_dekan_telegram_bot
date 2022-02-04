from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from data.config import GROUP_CHAT_ID, BOT_TOKEN

from keyboards.default.menu import tel_ru, menu_ru
from keyboards.inline.inline_btn_ru import language_ru, tekshir_ru
from states.state_data import PersonalData_ru
import re
from aiogram.dispatcher import filters
from aiogram import Bot, types

from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from filters import IsPrivate
from datetime import datetime

# import commands

bot=Bot(token=BOT_TOKEN)


PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




@dp.message_handler(IsPrivate(),text="👨🏼‍💼 О декане")
async def choose_lang(message:Message):
	await types.ChatActions.upload_photo()
	text = "Декан факультета телевизионных технологий, к.т.н.-Нарзуллоев Ойбек Мирзаевич"
	media = types.MediaGroup()
	media.attach_photo(types.InputFile('media\photo\dekan.JPG'), text)
	await message.answer_media_group(media)



@dp.message_handler(IsPrivate(),text="🌐 Изменить язык")
async def choose_lang(message:Message):

    await message.answer("O'zingizga qulay tilni tanlang!(🇺🇿/🇷🇺)\n-----\nВыберите удобный Вам язык!(🇺🇿/🇷🇺)",reply_markup=language_ru)
   


@dp.callback_query_handler(text="lang_ru")
async def uz_lang(call: CallbackQuery):
	text = "С помощью этого бота вы можете оставить свое Заявление, Жалобу и Предложение на имя декана Ташкентского факультета информационных технологий телевизионных технологий имени Мухаммада ал-Хоразмий!!!"

	await call.message.delete()
	await call.message.answer(text, reply_markup=menu_ru)
	await call.answer(cache_time=30)
	await call.answer()


@dp.message_handler(IsPrivate(),text="📝 Написать заявку",state=None)
async def ariza_yozish(message:Message):

    await message.answer("🧑🏻‍🎓 Имя и фамилия:",reply_markup=ReplyKeyboardRemove())
    await PersonalData_ru.name.set()



@dp.message_handler(state=PersonalData_ru.name)
async def answer_name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("👨‍👨‍👦‍👦 Введите вашу группу:")
    await PersonalData_ru.group.set()



@dp.message_handler(state=PersonalData_ru.group)
async def answer_group(message:Message,state:FSMContext):
    group = message.text
    await state.update_data(
        {"group":group}
    )
    await message.answer("📱 Введите свой номер телефона или отправьте контакт, нажав кнопку ниже:",reply_markup=tel_ru)
    await PersonalData_ru.phone_number.set()
   




@dp.message_handler(state=PersonalData_ru.phone_number, content_types="contact")
async def answer_phone(message:Message,state:FSMContext):
	phone_num = message
	

	if phone_num.contact:
	
		if re.search(PHONE_NUM,phone_num.contact.phone_number) :
        
			await state.update_data(
            	{"phone_number": phone_num.contact.phone_number}
            )
			await message.answer("📅 Введите текст заявки:",reply_markup=ReplyKeyboardRemove())
			await PersonalData_ru.ariza.set()
	
	elif 'text' in phone_num:
		if re.search(PHONE_NUM,phone_num.text):
            
			await state.update_data(
            	{"phone_number": phone_num.text}
            )
			await message.answer("📅 Введите текст заявки:",reply_markup=ReplyKeyboardRemove())
			await PersonalData_ru.ariza.set()
		else:
			await message.answer("❌ Вы набрали неверный номер!, \nВведите еще раз!")
			await PersonalData_ru.phone_number.set()



	else:
		await message.answer("❌ Вы набрали неверный номер!, \nВведите еще раз!")
		await PersonalData_ru.phone_number.set()





@dp.message_handler(state=PersonalData_ru.ariza)
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
    msg = "📌 Новое Заявление! \n\n"
    msg += f"🧑🏻‍🎓 Cтудент: {name}\n"
    msg += f"👨‍👨‍👦‍👦 Группа: {group}\n"
    msg += f"📱 Телефон номер: {phone_number}\n"
    msg += f"📝 Применение: {ariza}\n"
    msg += f"⏳ Bремя: {day}"

    await message.answer(msg)
    await state.finish()
    await message.answer("Вы отправите заявку?", reply_markup=tekshir_ru)




@dp.callback_query_handler(text="send_ru")
async def arizani_yuborish(call: CallbackQuery):
  
    await call.message.delete()
    await bot.send_message(GROUP_CHAT_ID, msg)

    await call.message.answer("✅ Ваша заявка отправлена!",reply_markup=menu_ru)
    await call.answer(cache_time=30)
    await call.answer()



@dp.callback_query_handler(text="wrong_ru")
async def arizani_bekor_qilish(call: CallbackQuery):
  
    await call.message.delete()
    await call.message.answer("❌ Ваша заявка была отменена!",reply_markup=menu_ru)
    await call.answer(cache_time=30)
    await call.answer()

