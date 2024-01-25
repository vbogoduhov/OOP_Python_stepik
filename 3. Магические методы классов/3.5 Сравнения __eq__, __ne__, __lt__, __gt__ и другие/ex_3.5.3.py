class Track(object):
    """docstring for Track."""

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lst_tracks = []
        # self.count = 0

    def __setattr__(self, key, value):
        if key in ["start_x", "start_y"]:
            if isinstance(value, (int, float)):
                object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.lst_tracks.append(tr)

    def get_tracks(self):
        return tuple(
            [TrackLine(self.start_x, self.start_y, self.lst_tracks[1].max_speed)]
            + self.lst_tracks
        )

    def __eq__(self, other):
        if isinstance(other, Track):
            # self.count += 1
            # print(self.count)
            return self.get_len_track() == other.get_len_track()

    def __gt__(self, other):
        if isinstance(other, Track):
            return self.get_len_track() > other.get_len_track()

    def __lt__(self, other):
        if isinstance(other, Track):
            return self.get_len_track() < other.get_len_track()

    def __len__(self):
        return self.get_len_track()

    def get_len_track(self):
        track_lenght = 0
        x = self.start_x
        y = self.start_y
        for line in self.lst_tracks:
            track_lenght += ((line.to_x - x) ** 2 + (line.to_y - y) ** 2) ** 0.5
            x, y = line.to_x, line.to_y
        return int(track_lenght)


class TrackLine(object):
    """docstring for TrackLine."""

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    def __setattr__(self, key, value):
        if key == "max_speed":
            if isinstance(value, int):
                object.__setattr__(self, key, value)

        else:
            if isinstance(value, (int, float)):
                object.__setattr__(self, key, value)


track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)
print(len(track1), len(track2))
