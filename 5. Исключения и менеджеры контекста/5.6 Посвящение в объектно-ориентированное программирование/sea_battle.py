class Ship(object):
    """Класс, описывающий корабль"""

    def __init__(self, length, tp=1, x=None, y=None):
        super(Ship, self).__init__()
        # сформировать локальные атрибуты
        self._x = x  # столбцы
        self._y = y  # строки
        self._length = length  # длина корабля
        self._tp = tp  # ориентция корабля
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

    def move(self, go):
        """Перемещение корабля на go клеток по направлению оринтации"""
        pass

    def is_collide(self, ship):
        """Проверка настолкновение с другим кораблём"""
        pass

    def is_out_pole(self, size):
        """Проверка на выход корабля за пределы игрового поля"""
        pass

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

    def init(self):
        """Инициализация игрового поля"""
        pass

    def get_ships(self):
        """Для получения коллекции _ships"""
        pass

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
