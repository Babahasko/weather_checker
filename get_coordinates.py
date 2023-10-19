from typing import NamedTuple, Literal
from exceptions import CantGetCoordinates
import config
import ipinfo


class Coordinates(NamedTuple):
    longitude: float
    latitude: float


def get_coordinates() -> Coordinates:
    ipinfo_dict = _get_ipinfo()
    coordinates = _parse_ipinfo_dict(ipinfo_dict)
    return _round_cords(coordinates)


def _get_ipinfo() -> dict:
    try:
        handler = ipinfo.getHandler(config.IPINFO_API)
        ipinfo_dict = handler.getDetails().all
        return ipinfo_dict
    except Exception:
        raise CantGetCoordinates


def _parse_ipinfo_dict(ipinfo_dict: dict) -> Coordinates:
    try:
        return Coordinates(
            latitude=_parse_coord(ipinfo_dict, "latitude"),
            longitude=_parse_coord(ipinfo_dict, "longitude")
        )
    except Exception:
        raise CantGetCoordinates


def _parse_coord(ipinfo_dict: dict,
                 coord_type: Literal["longitude"] | Literal["latitude"]) -> float:
    try:
        coordinate = ipinfo_dict[f"{coord_type}"]
        return _float_coordinate(coordinate)
    except Exception:
        raise CantGetCoordinates


def _float_coordinate(value: str) -> float:
    try:
        return float(value)
    except Exception:
        raise CantGetCoordinates


def _round_cords(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 4),
        [coordinates.longitude, coordinates.latitude]
    ))


if __name__ == "__main__":
    print(get_coordinates())
