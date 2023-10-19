class ApiServiceError(Exception):
    """Program can`t get current weather"""


class CantGetCoordinates(Exception):
    """Program can`t get GPS coordinates"""
