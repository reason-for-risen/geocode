from itertools import count
from geopy import Location, get_geocoder_for_service, Nominatim

from src.utils import configure_ssl


class Locator:
    def __init__(self, service="nominatim"):
        configure_ssl()
        self.locator = get_geocoder_for_service(service)(user_agent='mygeoapp')

    def from_query(self, query):
        return self.locator.geocode(query)

    def from_coordinates(self, latitude, longitude):
        return self.locator.reverse((latitude, longitude))


class Marker:
    _ids = count(0)

    def __init__(self, location: Location):
        self.id = next(self._ids)
        self.lat = location.latitude
        self.lon = location.longitude
        self.popup_msg = str(location)

    @property
    def popup(self):
        return f'$(`<div id="html_{self.id}" style="width: 100.0%; height: 100.0%;">{self.popup_msg}</div>`)[0];'

    def __str__(self):
        return f'Marker at {self.popup_msg}'
