import shelve
import geo_req


def add(chat_id, username, first_name, bot):
    with shelve.open('people-shelve') as db:
        user = {
            'username': username,
            'first_name': first_name,
            'location': None,
        }
        db[str(chat_id)] = user

    geo_req.req(chat_id, bot)
