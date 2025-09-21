
import telebot

API_TOKEN = "8492754430:AAE641TL8sqA6GofIGnhbphFPhHPvlXLd7E"
ADMIN_ID = 1997381929

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the GoldCoin Airdrop Bot! 🌟\nCollect points by completing tasks and invite friends to earn rewards.")

@bot.message_handler(commands=['points'])
def points(message):
    bot.send_message(message.chat.id, "You currently have 0 points. 🚀")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Commands:\n/start - Start the bot\n/points - Check your points\n/help - Help menu")

print("Bot is running...")
bot.polling()
