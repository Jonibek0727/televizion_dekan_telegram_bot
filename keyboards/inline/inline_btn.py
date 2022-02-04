from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang_data = {
    "🇺🇿 Uz":"lang_uz",
    "🇷🇺 Ru":"lang_ru"
}


language = InlineKeyboardMarkup(row_width=2)

for key, value in lang_data.items():
    language.insert(InlineKeyboardButton(text=key, callback_data=value))




# ariza_yoz = InlineKeyboardMarkup(row_width=1)
# ariza_yoz.insert(InlineKeyboardButton(text="📝 Ariza yozish", callback_data="ariza_yozish"))

tekshir = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Ha", callback_data="send"),
		InlineKeyboardButton(text="❌ Yo'q", callback_data="wrong"),
	],
])


