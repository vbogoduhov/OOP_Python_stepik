class Ship(object):
    """Класс, описывающий корабль"""

    def __init__(self, length, tp=1, x=None, y=None):
        super(Ship, self).__init__()
        # сформировать локальные атрибуты
        self._x = x  # столбцы
        self._y = y  # строки
        self._length = length  # длина корабля
        self._tp = tp  # ориентция корабля 1 - горизонтальная, 2 - вертикальная
        self._cells = [
            1 for _ in range(self._length)
        ]  # коллекция хранит попадания/промахи - 1 -- промах, 2 -- попадание
        self._is_move = True  # флаг возможности перемещения корабля

    def set_start_coords(self, x, y):
        """Установка начальных кородинат для корабля"""
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Координаты должны быть числами")
        self._x = x
        self._y = y

    def get_start_coords(self):
        """Получение начальных координат корабля в виде кортежа"""
        return (self._x, self._y)

    def move(self, go=1):
        """Перемещение корабля на go клеток по направлению ориентации"""
        if self._is_move:
            if self._tp == 1:
                self.set_start_coords(self._x + go, self._y)
            else:
                self.set_start_coords(self._x, self._y + go)

    def is_collide(self, ship):
        """Проверка настолкновение с другим кораблём"""
        ship_coord = ship.get_start_coords()
        if self._tp == ship._tp:  # Ориентация кораблей одинакова
            if self._tp == 1:  # Ориентация кораблей горизонтальна
                if not (
                    abs(self._y - ship_coord[1]) > 1
                    or (ship_coord[0] - (self._x + self._length - 1)) > 1
                    or (self._x - (ship_coord[0] + ship._length - 1)) > 1
                ):
                    return True
            else:  # Ориентация кораблей вертикальна
                if not (
                    abs(self._x - ship_coord[0]) > 1
                    or (ship_coord[1] - (self._y + self._length - 1)) > 1
                    or (self._y - (ship_coord[1] + ship._length - 1)) > 1
                ):
                    return True
        elif (
            self._tp == 1 and ship_tp == 2
        ):  # Ориентация кораблей не одинакова, текущий - горизонтальный, второй - вертикальный
            if not (
                (ship_coord[1] - self._y) > 1
                or (self._y - (ship_coord[1] + ship._length - 1)) > 1
                or (ship_coord[0] - (self._x + self._length - 1)) > 1
                or (self._x - ship_coord[0]) > 1
            ):
                return True
        else:  # Ориентация не одинакова, текущий - вертикальный, воторой - горизонтальный
            if not (
                (ship_coord[1] - (self._y + self._length - 1)) > 1
                or (self._y - ship_coord[1]) > 1
                or (ship_coord[0] - (self._x + self._length - 1)) > 1
                or (self._x - ship_coord[0]) > 1
            ):
                return True
        return False

    def is_out_pole(self, size):
        """Проверка на выход корабля за пределы игрового поля"""
        if self._x + self._length > size or self._y + self._length > size:
            return True
        return False

    def __getitem__(self, key):
        """Доступ к коллекции _cells по индексу"""
        if key < 0 or key > len(self._cells) - 1:
            raise IndexError("Неверный индекс")
        return self._cells[key]

    def __setitem__(self, key, value):
        """Доступ к коллекции _cells по индексу"""
        if key < 0 or key > len(self._cells) - 1:
            raise IndexError("Неверный индекс")
        if value not in (1, 2):
            raise ValueError("Неверное значение для коллекции _cells")
        self._cells[key] = value


class GamePole(object):
    """Класс, описывающий игровое поле"""

    def __init__(self, size=10):
        super(GamePole, self).__init__()
        self._ships = []
        self._size = size

    def init(self):
        """Инициализация игрового поля"""
        pass

    def get_ships(self):
        """Для получения коллекции _ships"""
        return self._ships

    def move_ships(self):
        """Перемещает все корабли на одну клетку по напраалению оринтации"""
        pass

    def show(self):
        """Отображение игрового поля в консоли.
        Каждый корабль должен отображаться значениями из коллекции _cells"""
        pass

    def get_pole(self):
        """Получение текущего игрового поля в виде двумерного кортежа"""
        pass
