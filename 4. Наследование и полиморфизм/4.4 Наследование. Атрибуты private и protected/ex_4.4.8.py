class Aircraft(object):
    """docstring for Aircraft."""

    def __init__(self, model, mass, speed, top):
        super(Aircraft, self).__init__()
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if (
            (key == "_model" and not isinstance(value, str))
            or (key == "_mass" and (not isinstance(value, (float, int)) or value < 0))
            or (key == "_speed" and (not isinstance(value, (float, int)) or value < 0))
            or (key == "_top" and (not isinstance(value, (float, int)) or value < 0))
        ):
            raise TypeError("неверный тип аргумента")
        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):
    """docstring for PassengerAircraft."""

    def __init__(self, model, mass, speed, top, chairs):
        super(PassengerAircraft, self).__init__(model, mass, speed, top)
        if not isinstance(chairs, int) or chairs < 0:
            raise TypeError("неверный тип аргумента")
        self._chairs = chairs


class WarPlane(Aircraft):
    """docstring for WarPlane."""

    def __init__(self, model, mass, speed, top, weapons):
        super(WarPlane, self).__init__(model, mass, speed, top)
        if not isinstance(weapons, dict):
            raise TypeError("неверный тип аргумента")
        self._weapons = weapons


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 2500, 2000, {"ракета": 4, "бомба": 11}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]

