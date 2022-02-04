from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Telefon raqamimni yuborish",request_contact=True),           
        ],
    ],
    resize_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Ariza yozish"),           
            KeyboardButton(text="👨🏼‍💼 Dekan haqida"),           
             
        ],
        [
            KeyboardButton(text="🌐 Tilni o'zgartirish"), 
        ],
    ],
    resize_keyboard=True
)



tel_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Отправить мой номер телефона",request_contact=True),           
        ],
    ],
    resize_keyboard=True
)


menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Написать заявку"),           
            KeyboardButton(text="👨🏼‍💼 О декане"),           
             
        ],
        [
            KeyboardButton(text="🌐 Изменить язык"), 
        ],
    ],
    resize_keyboard=True
)

