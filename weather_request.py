import shelve
import weather_API
import weather_codes


def req(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
    current_weather = weather_API.get_weather(
        user['location']['latitude'],
        user['location']['longitude'],
    )

    format_string = 'Текущая погода для вашей местности\n\n' \
                    '{condition}\n' \
                    'Температура: {temp}℃\n' \
                    'Ощущается на: {feels_like}℃\n' \
                    'Влажность: {humidity}%\n' \
                    'Давление: {pressure_mm} мм рт.ст.\n' \
                    'Ветер: {wind_speed} м/с, {wind_dir}'

    return format_string.format(
        condition=weather_codes.CONDITION[current_weather['fact']['condition']],
        temp=current_weather['fact']['temp'],
        feels_like=current_weather['fact']['feels_like'],
        humidity=current_weather['fact']['humidity'],
        pressure_mm=current_weather['fact']['pressure_mm'],
        wind_speed=current_weather['fact']['wind_speed'],
        wind_dir=weather_codes.WIND_DIR[current_weather['fact']['wind_dir']],
    )
