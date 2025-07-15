import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

API_TOKEN = "7735624977:AAEkS_-yYB1-Ug0ejJhp9RqHeQFU0b0dr-E"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ref_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="🆕 Нова грааа", url="https://lhcets.life/?oopen=register&c=czh")
)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привіт, брат\n"
        "Один брат ото писав, як заробив з телефоном 8к\n\n"
        "Пиши команду /go і бери участь, цікаві виплати\n\n"
        "🧠 Пиши команду, щоб спробувати",
        reply_markup=ref_button
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
