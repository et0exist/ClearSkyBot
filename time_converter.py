from datetime import datetime
from datetime import timezone
import pytz
import requests


def utc_to_local(utc_unix, latitude, longitude):
    utc_dt = datetime.fromtimestamp(utc_unix)
    url = 'http://api.geonames.org/timezoneJSON'
    request = requests.get(
        url,
        params={
            'lat': latitude,
            'lng': longitude,
            'username': 'et0exist',
        }
    )
    timezone_str = request.json()['timezoneId']
    local_tz = pytz.timezone(timezone_str)
    time = utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=local_tz)
    time_str = '{day:02}.{month:02}.{year}, {time!s}'.format(
        day=time.day,
        month=time.month,
        year=time.year,
        time=time.time(),
    )
    return time_str
