from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang_data = {
    "๐บ๐ฟ ะฃะท":"lang_uz",
    "๐ท๐บ ะ ั":"lang_ru"
}


language_ru = InlineKeyboardMarkup(row_width=2)

for key, value in lang_data.items():
    language_ru.insert(InlineKeyboardButton(text=key, callback_data=value))




# ariza_yoz = InlineKeyboardMarkup(row_width=1)
# ariza_yoz.insert(InlineKeyboardButton(text="๐ Ariza yozish", callback_data="ariza_yozish"))

tekshir_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="โ ะะฐ", callback_data="send_ru"),
		InlineKeyboardButton(text="โ ะะตั", callback_data="wrong_ru"),
	],
])


