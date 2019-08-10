import pytest


from geopy import Nominatim

from src.marker import Locator


def test_locator():
    geocoder = Locator()
    assert isinstance(geocoder.locator, Nominatim)


def test_add():
    assert 2 + 2 == 4


