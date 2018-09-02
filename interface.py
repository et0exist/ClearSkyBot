import new_user
import keyboard_buttons
import geolocation_response
import satellites_request
import weather_request
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove


class Parser:
    def __init__(self, chat_id, content_type, msg, bot):
        self.chat_id = chat_id
        self.content_type = content_type
        self.msg = msg
        self.bot = bot

    def parse(self):
        def geo_request(chat_id, bot):
            kb_geo_req = ReplyKeyboardMarkup(
                keyboard=[
                    [keyboard_buttons.send_geo]
                ],
                resize_keyboard=True,
            )

            bot.sendMessage(
                chat_id,
                'Для получения интересующей вас информации, необходимо знать'
                ' вашу геолокацию.',
                reply_markup=kb_geo_req,
            )

        def to_new_user(chat_id, msg, bot):
            new_user.add(chat_id, msg)
            geo_request(chat_id, bot)

        def to_geo_response(chat_id, msg, bot):
            geolocation_response.add(chat_id, msg)
            # kb_remove = ReplyKeyboardRemove()
            # bot.sendMessage(
            #     chat_id,
            #     text='Координаты обновлены.',
            #     reply_markup=kb_remove,
            # )

            kb_sat_req = ReplyKeyboardMarkup(
                keyboard=[
                    [keyboard_buttons.send_sat],
                    [keyboard_buttons.send_weather],
                    [keyboard_buttons.update_geo],
                ],
                resize_keyboard=True,
            )
            bot.sendMessage(
                chat_id,
                text='Координаты обновлены.',
                reply_markup=kb_sat_req,
            )

        def to_sat_request(chat_id, msg):
            return satellites_request.req(chat_id, msg)

        def to_weather_request(chat_id, msg):
            return weather_request.req(chat_id, msg)

        parse_dict = {
            'Получить информацию о пролетах': to_sat_request,
            'Получить информацию о погоде': to_weather_request,
        }

        if self.content_type == 'location':
            to_geo_response(self.chat_id, self.msg, self.bot)
        elif self.msg['text'] == '/start':
            to_new_user(self.chat_id, self.msg, self.bot)
        else:
            to_user = parse_dict[self.msg['text']](self.chat_id, self.msg)
            self.bot.sendMessage(self.chat_id, to_user)
