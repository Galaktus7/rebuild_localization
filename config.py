import telebot
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)

cwbottoken = os.environ['CW_BOT_TOKEN']
cwbottoken_bot = telebot.TeleBot(cwbottoken)

cwlogstoken = os.environ['CW_LOGS_TOKEN']
cwlogstoken_bot = telebot.TeleBot(cwlogstoken)

testbot = os.environ['TEST_BOT_TOKEN']
testbot_bot = telebot.TeleBot(testbot)

database = os.environ['MONGO_DB']
database2 = os.environ['MONGO_DB_2']
