from  aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
bot = Bot('6731513345:AAHiPB9CLM89itWbIMb_4rQdF67CxYMuwiA')
dp = Dispatcher(bot)
knopka = InlineKeyboardMarkup()
knopka.add(
    InlineKeyboardButton(text='Ovoz berish',
                         url='https://t.me/ochiqbudjet_07_bot?start=048355958011')
)
@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid,
                           text='Xush kelibsiz. Ovoz berish uchun knopkani bosing.',
                           reply_markup=knopka)
executor.start_polling(dp, skip_updates=True)