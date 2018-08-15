import shelve


def add(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
        user['location'] = msg['location']
        db[str(chat_id)] = user
