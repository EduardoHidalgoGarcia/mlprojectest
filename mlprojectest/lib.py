import requests

def get_coordinates(address):
    url = "https://nominatim.openstreetmap.org/search" #endpoint
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(url, params).json()
    return [response[0]['lat'], response[0]['lon']]