import shelve


def add(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = {
            'username': msg['chat']['username'],
            'first_name': msg['chat']['first_name'],
            'location': None,
        }
        db[str(chat_id)] = user
