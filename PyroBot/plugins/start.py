from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton  


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hello there!",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.private & filters.command(["key"]))

async def start(bot, message):

		.send_message( message.chat.id, "This is a ReplyKeyboardMarkup example", reply_markup=ReplyKeyboardMarkup( [ ["A", "B", "C", "D"],["E", "F", "G"],["H", "I"],["J"]], resize_keyboard=True ) )
