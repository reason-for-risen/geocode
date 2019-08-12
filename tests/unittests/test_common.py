import pytest


from geopy import Nominatim

from src.marker import Locator


def test_locator():
    geocoder = Locator()
    assert isinstance(geocoder.locator, Nominatim)

