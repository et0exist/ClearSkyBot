#!/usr/bin/python
import telepot
import new_user
import geo_rcv
import sat_req
import time


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'location':
        geo_rcv.add(
            chat_id,
            msg['location'],
            bot,
        )
    elif msg['text'] == '/start':
        new_user.add(
            chat_id,
            msg['chat']['username'],
            msg['chat']['first_name'],
            bot,
        )
    elif msg['text'] == 'Получить информацию о пролетах':
        sat_req.req(chat_id, bot)


bot = telepot.Bot('520748932:AAECql5-CE6lLqzo09uzoiwTUiOaaWo4SmY')
bot.message_loop(handle)
print('Listening ...')
while 1:
    time.sleep(10)
