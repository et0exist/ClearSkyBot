import shelve
import API


def req(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
    # Временные переменные. Сделать так, чтобы они задавались
    # либо пользователем, либо автоматически
    norad_id = 25544
    days = 20
    min_visibility = 300

    passes = API.get_visual_passes(
        norad_id,
        user['location']['latitude'],
        user['location']['longitude'],
        days,
        min_visibility,
    )

    return 'Ближайший пролет произойдет {} в направлении азимута {}, с высотой над горизонтом {}'.format(
        passes['passes'][0]['startUTC'],
        passes['passes'][0]['startAz'],
        passes['passes'][0]['startEl'],
    )
