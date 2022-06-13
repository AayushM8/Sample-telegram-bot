from turtle import up, update
import constants as keys 
from telegram.ext import * 
import responses as R
import time
from telegram import *
from telegram.ext import * 
from requests import *
# updater = Updater (token="5405683249:AAGktC6cqbAYOa2-aTChPPDBb7ej5gCazlY") 
# dispatcher = updater.dispatcher
# def startCommand (update: Update, context: CallbackContext):
#     buttons = [[KeyboardButton( "Permanent Address")] [KeyboardButton("Office Address")]] 
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my boti", 

#     reply_markup=ReplyKeyboardMarkup (buttons))


print("Bot started...")

def start_command (update, context): 
    update.message.reply_text('''Type something random to get started!\n Which address would you like to choose?''')
    buttons = [[KeyboardButton( "Permanent Address")], [KeyboardButton("Office Address")]] 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my boti", 

    reply_markup=ReplyKeyboardMarkup (buttons))

def help_command (update, context): 
    update.message.reply_text('If you need help! You should ask for it on Google!')
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)
count=0
def handle_message(update, context):
    text = str(update.message.text).lower()     
    response = R.sample_responses (text)

    update.message.reply_text(response)

# def messageHandler(update, context):
    if update.message.text=="Office Address" or update.message.text=="Permanent Address":
        print('recieved')
        buttons = [[KeyboardButton( "Add New Address")], [KeyboardButton("Update Address")]] 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Enter the new address/Update Address", 

        reply_markup=ReplyKeyboardMarkup (buttons))
    if update.message.text=="Add New Address" or update.message.text=="Update Address":
            
            response=R.sample_responses("padd")
            update.message.reply_text(response)
            print("accessed")
            count=1
            print(count,"inside")
    print(count)
    if count==1:
        response=R.sample_responses("hno")
        update.message.reply_text(response)
        print(count, "hno")
        count=2
        time.sleep(15)
    if count==2:
        response=R.sample_responses("hname")
        update.message.reply_text(response)
        count=3
        time.sleep(15)
    if count==3:
        response=R.sample_responses("sname")
        update.message.reply_text(response)
        count==4
        time.sleep(15)
    if count==4:
        response=R.sample_responses("cname")



        





def error(update, context):
    print(f"Update {update} caused error {context.error}")
def main():
    updater = Updater(keys. API_KEY, use_context=True) 
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command)) 
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling() 
    updater.idle()
main()







# markup = ReplyKeyboardMarkup(keyboard=[['Time', KeyboardButton(text='Logo')],["File", "Audio"]])
#     if command == '/start':
#         telegram_bot.sendMessage (chat_id, str("Hi! Which one do you want? choose from the below keyboard buttons."), reply_markup=markup)
#         telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))

# dispatcher.add_handler(CommandHandler("start", start_command))
# updater.start_polling()

