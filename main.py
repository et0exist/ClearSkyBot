#!/usr/bin/python
import interface
import telepot
import time

with open('ClearSkyBot_token') as f:
    token = f.read()
bot = telepot.Bot(token)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    update = interface.Parser(chat_id, content_type, msg, bot)
    update.parse()


bot.message_loop(handle)
print('Listening ...')
while 1:
    time.sleep(10)
