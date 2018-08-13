import shelve


def req(chat_id, bot):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]

    # здесь нужен вызов метода, который определит по API, где искать яркие спутники

    bot.sendMessage(
        chat_id,
        'Ваши координаты: {}, {}'.format(
            user['location']['latitude'],
            user['location']['longitude'],
        )
    )
