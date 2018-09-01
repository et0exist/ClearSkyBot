import requests

with open('satellites_API_key') as key:
    api_key = key.read()
base_url = 'https://www.n2yo.com/rest/v1/satellite/'


def get_altitude(latitude, longitude):
    pass


def get_tle(norad_id):
    url = base_url + 'tle/{}/'.format(norad_id)
    tle = requests.get(url, params={'apiKey': api_key})
    return tle.json()


def get_satellite_positions(norad_id, latitude, longitude, seconds):
    altitude = 0
    # altitude = get_altitude(latitude, longitude)
    url = base_url + 'positions/{}/{}/{}/{}/{}'.format(
        norad_id,
        latitude,
        longitude,
        altitude,
        seconds,
    )
    satellite_positions = requests.get(url, params={'apiKey': api_key})
    return satellite_positions.json()


def get_visual_passes(norad_id, latitude, longitude, days, min_visibility):
    altitude = 0
    # altitude = get_altitude(latitude, longitude)
    url = base_url + 'visualpasses/{}/{}/{}/{}/{}/{}'.format(
        norad_id,
        latitude,
        longitude,
        altitude,
        days,
        min_visibility,
    )
    visual_passes = requests.get(url, params={'apiKey': api_key})
    return visual_passes.json()


def get_radio_passes(norad_id, latitude, longitude, days, min_elevation):
    altitude = 0
    # altitude = get_altitude(latitude, longitude)
    url = base_url + 'radiopasses/{}/{}/{}/{}/{}/{}'.format(
        norad_id,
        latitude,
        longitude,
        altitude,
        days,
        min_elevation,
    )
    radio_passes = requests.get(url, params={'apiKey': api_key})
    return radio_passes.json()


def above(latitude, longitude, search_radius, category_id=0):
    altitude = 0
    # altitude = get_altitude(latitude, longitude)
    url = base_url + 'above/{}/{}/{}/{}/{}'.format(
        latitude,
        longitude,
        altitude,
        search_radius,
        category_id,
    )
    above = requests.get(url, params={'apiKey': api_key})
    return above.json()
