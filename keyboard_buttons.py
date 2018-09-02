from telepot.namedtuple import KeyboardButton

send_geo = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True,
)

update_geo = KeyboardButton(
    text='Обновить геолокацию',
    request_location=True,
)

send_sat = KeyboardButton(
    text='Получить информацию о пролетах',
)

send_weather = KeyboardButton(
    text='Получить информацию о погоде',
)
