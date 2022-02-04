from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang_data = {
    "🇺🇿 Уз":"lang_uz",
    "🇷🇺 Ру":"lang_ru"
}


language_ru = InlineKeyboardMarkup(row_width=2)

for key, value in lang_data.items():
    language_ru.insert(InlineKeyboardButton(text=key, callback_data=value))




# ariza_yoz = InlineKeyboardMarkup(row_width=1)
# ariza_yoz.insert(InlineKeyboardButton(text="📝 Ariza yozish", callback_data="ariza_yozish"))

tekshir_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Да", callback_data="send_ru"),
		InlineKeyboardButton(text="❌ Нет", callback_data="wrong_ru"),
	],
])


