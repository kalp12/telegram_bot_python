from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

updater = Updater(token= Api key needed)
dispatcher=updater.dispatcher

def start(update,context):
    bot=context.bot
    bot.send_message(chat_id=update.effective_chat.id,text="Hello welcome to newxyz")
dispatcher.add_handler(CommandHandler("start",start))

def echo(update,context):
    context.bot.sendMessage(chat_id=update.message.chat_id,text=update.message.text.upper())
dispatcher.add_handler(MessageHandler(Filters.text,echo))

def option(update,context):
    keyboard = [
                [InlineKeyboardButton("Click button 1", callback_data='callback_1'),
                InlineKeyboardButton("Click button 2", callback_data='callback_2')],
                [InlineKeyboardButton("Click button 3", callback_data='callback_3')]
            ]
    reply_markup =InlineKeyboardMarkup(keyboard)
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Text One",reply_markup=reply_markup)
dispatcher.add_handler(CommandHandler("option",option))

def button(update,context):
    query=update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                text="Thank You For choosing {}".format(query.data),
                                message_id=query.message.message_id)
dispatcher.add_handler(CallbackQueryHandler(button))

def get_location(update,context):
    button=[
        [KeyboardButton("Share Location",request_location=True)]
        ]
    reply_markup=ReplyKeyboardMarkup(button)
    context.bot.sendMessage(chat_id=update.message.chat_id,
                    text="Mind sharing Location",
                    reply_markup=reply_markup)
dispatcher.add_handler(CommandHandler("location",get_location))

def location(update,context):
    lat=update.message.location.latitude
    lon=update.message.location.longitude
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Longitude :{} Latitude :{}".format(lon,lat),
                            reply_markup=ReplyKeyboardRemove())
dispatcher.add_handler(MessageHandler(Filters.location,location))

updater.start_polling()
