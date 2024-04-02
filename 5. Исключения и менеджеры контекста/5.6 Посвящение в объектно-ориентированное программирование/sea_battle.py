from random import randint


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
            self._tp == 1 and ship._tp == 2
        ):  # Ориентация кораблей не одинакова, текущий - горизонтальный, второй - вертикальный
            if not (
                (ship_coord[1] - self._y) > 1
                or (self._y - (ship_coord[1] + ship._length - 1)) > 1
                or (ship_coord[0] - (self._x + self._length - 1)) > 1
                or (self._x - ship_coord[0]) > 1
            ):
                return True
        else:  # Ориентация не одинакова, текущий - вертикальный, второй - горизонтальный
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

    def __eq__(self, ship):
        coord = ship.get_start_coords()
        if (
            self._length == ship._length
            and self._tp == ship._tp
            and self._x == coord[0]
            and self._y == coord[1]
        ):
            return True
        return False

    def get_incremental_coord(self, step):
        if self._tp == 1:
            return self._x + step, self._y
        return self._x, self._y + step


class GamePole(object):
    """Класс, описывающий игровое поле"""

    def __init__(self, size=10):
        super(GamePole, self).__init__()
        self._ships = []
        self._size = size

    def init(self):
        """Инициализация игрового поля"""
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
        ]
        # Теперь нужно расставить корабли
        self.__shuffle_ships()

    def __shuffle_ships(self):
        count = 0
        while count < self._size:
            ship = self._ships[count]
            while True:
                ship.set_start_coords(randint(0, 9), randint(0, 9))
                if self.is_not_collide_all(
                    ship, self._ships[:count]
                ) and not ship.is_out_pole(self._size):
                    break
            count += 1

    def is_not_collide_all(self, ship, lst_ships=None):
        if lst_ships is None:
            lst = self._ships
        else:
            lst = lst_ships
        for other in lst:
            if ship != other:
                if ship.is_collide(other):
                    return False
        return True

    def get_ships(self):
        """Для получения коллекции _ships"""
        return self._ships

    def move_ships(self):
        """Перемещает все корабли на одну клетку по направлению ориентации"""
        for ship in self._ships:
            coord = ship.get_start_coords()
            # продумать как автоматически увеличивать нужнуюю координату на нужное количество клеток, в зависимости от ориентации
            new_coord = ship.get_incremental_coord(1)
            ship.set_start_coords(new_coord[0], new_coord[1])
            if self.is_not_collide_all(ship) and not ship.is_out_pole(self._size):
                ship.set_start_coords(coord[0], coord[1])
                ship.move(1)
            else:
                new_coord = ship.get_incremental_coord(-2)
                ship.set_start_coords(new_coord[0], new_coord[1])
                if self.is_not_collide_all(ship) and not ship.is_out_pole(self._size):
                    ship.set_start_coords(coord[0], coord[1])
                    ship.move(-1)
                else:
                    ship.set_start_coords(coord[0], coord[1])

    def show(self):
        """Отображение игрового поля в консоли.
        Каждый корабль должен отображаться значениями из коллекции _cells"""
        pole = self.get_pole()

        for row in pole:
            print(*row)

    def get_pole(self):
        """Получение текущего игрового поля в виде двумерного кортежа"""
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            coord = ship.get_start_coords()
            length = ship._length
            tp = ship._tp
            cells = ship._cells
            if tp == 1:
                for x, v in enumerate(cells):
                    pole[coord[1]][coord[0] + x] = v
            else:
                for x, v in enumerate(cells):
                    pole[coord[1] + x][coord[0]] = v
        out = tuple([tuple([i for i in row]) for row in pole])
        return out


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
