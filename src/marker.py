from itertools import count

from geopy import Location


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
