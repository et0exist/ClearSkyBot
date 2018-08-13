from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def req(chat_id, bot):
    kb_geo_req = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text='Отправить геолокацию',
                    request_location=True,
                )
            ]
        ],
        resize_keyboard=True,
    )
    bot.sendMessage(
        chat_id,
        'Для того, чтобы определить время и место пролетов для вашей местности, нам необходимо знать ваши координаты.',
        reply_markup=kb_geo_req,
    )
