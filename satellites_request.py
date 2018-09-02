import shelve
import satellites_API
import time_converter


def req(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
    # Временные переменные
    norad_id = 25544
    days = 20
    min_visibility = 300

    passes = satellites_API.get_visual_passes(
        norad_id,
        user['location']['latitude'],
        user['location']['longitude'],
        days,
        min_visibility,
    )

    format_string = 'Ближайший пролет произойдет {startUTC} в направлении ' \
                    'азимута {startAz}°, с высотой над горизонтом {startEl}°'

    return format_string.format(
        startUTC=time_converter.utc_to_local(
            utc_unix=passes['passes'][0]['startUTC'],
            latitude=user['location']['latitude'],
            longitude=user['location']['longitude'],
        ),
        startAz=passes['passes'][0]['startAz'],
        startEl=passes['passes'][0]['startEl'],
    )
