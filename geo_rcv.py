import shelve
from telepot.namedtuple import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


def add(chat_id, location, bot):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
        user['location'] = location
        db[str(chat_id)] = user

    kb_remove = ReplyKeyboardRemove()
    bot.sendMessage(
        chat_id,
        text='Координаты обновлены.',
        reply_markup=kb_remove,
    )

    kb_sat_req = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Получить информацию о пролетах',)],
            [KeyboardButton(text='Обновить геолокацию', request_location=True,)]],
        resize_keyboard=True,
    )
    bot.sendMessage(
        chat_id,
        text='Теперь вы можете получить информацию о предстоящих пролетах ярких спутников.',
        reply_markup=kb_sat_req,
    )
