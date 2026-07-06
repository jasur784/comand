import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart , Command 
from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()

Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Payment"),KeyboardButton(text='Axmet'),KeyboardButton(text="Amir"),
            KeyboardButton(text="Samandar")
        ]
    ],
    resize_keyboard=True,
    )
@dp.message()
async def hh(message:Message):
    amirr = message.text
    if amirr=='Amir':
        await message.answer('Amir Amanbekov')

@dp.message(F.text == "📚 Kitaplar")
async def books(message: Message):
    await message.answer("Kitaplar bo'limi.")

@dp.message(F.text == "📝 Bánt etiw")
async def borrow(message: Message):
    await message.answer("Bánt etiw bo'limi.")

@dp.message(F.text == "⏰ Qaytarıw múddeti")
async def return_date(message: Message):
    await message.answer("Qaytarıw múddeti bo'limi.")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello')
@dp.message(Command(commands=["payment"]))
async def payment(message: Message):
    await message.answer('Payment command received!',reply_markup=Keyboard)
@dp.message()
async def menu(message:Message):
    text = message.text
    if text=='Axmet':
        await message.answer('Axmet Muratbaev')
    elif text == "Samandar":
        await message.answer("Qdirbaev Samandar")    
 

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())