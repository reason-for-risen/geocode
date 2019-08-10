from geopy import Nominatim, Location
import ssl


def configure_ssl():
    # Disable SSL certificate verification
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context


def get_location(text) -> Location:
    configure_ssl()
    locator = Nominatim(user_agent='geoapp')
    return locator.geocode(text)
