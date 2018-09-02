import shelve
import weather_API

def req(chat_id, msg):
    with shelve.open('people-shelve') as db:
        user = db[str(chat_id)]
    # Нужно добавить