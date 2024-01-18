class Clock(object):
    """Класс, представляющий объект времени"""

    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __setattr__(self, key, value):
        if isinstance(value, int) and value > 0:
            object.__setattr__(self, key, value)

    def get_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

    @property
    def hours(self):
        """The hours property."""
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value

    @property
    def minutes(self):
        """The minutes property."""
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._minutes = value

    @property
    def seconds(self):
        """The seconds property."""
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        self._seconds = value


class DeltaClock(object):
    """Класс возвращает разницу во времени
    между двумя объектами типа Clock"""

    def __init__(self, clock1, clock2):
        super(DeltaClock, self).__init__()
        self._clock1 = clock1
        self._clock2 = clock2

    def __len__(self):
        return (
            self._clock1.get_time() - self._clock2.get_time()
            if (self._clock1.get_time() - self._clock2.get_time()) > 0
            else 0
        )

    def __str__(self):
        h = self._clock1.hours - self._clock2.hours
        m = self._clock1.minutes - self._clock2.minutes
        s = self._clock1.seconds - self._clock2.seconds
        return f"{h if h > 0 else 0:0{2}}: {m if m > 0 else 0:0{2}}: {s if s > 0 else 0:0{2}}"


dt = DeltaClock(Clock(5, 45, 32), Clock(2, 23, 12))
print(dt)
print(len(dt))
dt1 = DeltaClock(Clock(2, 32, 12), Clock(5, 32, 32))
print(dt1)
