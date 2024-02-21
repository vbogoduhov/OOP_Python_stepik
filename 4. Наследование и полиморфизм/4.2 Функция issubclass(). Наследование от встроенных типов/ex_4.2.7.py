class VideoItem(object):
    """docstring for VideoItem."""

    def __init__(self, title, descr, path):
        super(VideoItem, self).__init__()
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating(object):
    """docstring for VideoRating."""

    MIN_RATING = 0
    MAX_RATING = 5

    def __init__(self, rating=0):
        super(VideoRating, self).__init__()
        self.__rating = rating

    def __setattr__(self, key, value):
        if key == "rating":
            if (
                not isinstance(value, int)
                or (value < self.MIN_RATING)
                or (value > self.MAX_RATING)
            ):
                raise ValueError("неверное присваиваемое значение")
        object.__setattr__(self, key, value)

    @property
    def rating(self):
        """The rating property."""
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value


v = VideoItem(
    "Курс по Python ООП", "Подробный курс по Python ООР", "D:/videos/python_oop.mp4"
)
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError
