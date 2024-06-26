# Посвящение в ООП

Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным лишь избранных!

Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в объектно-ориентированное программирование.

И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть.
Поэтому они решили дать задание своим программистам написать программу игры "Морской бой".
Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле _10 х 10_ клеток и расставляет на нем десять кораблей:

- однопалубных - 4;

- двухпалубных - 3;

- трехпалубных - 2;

- четырехпалубный - 1.


Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы.
И отмечают эти выстрелы на другом таком же поле в 10 х 10 клеток, которое представляет поле соперника.

Соперник при этом должен честно отвечать: "промах", если ни один корабль не был задет и "попал", если произошло попадание.
Выигрывает тот игрок, который первым поразит все корабли соперника.

Но это была игра из глубокого прошлого.
Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само задание звучит так.

## Техническое задание
В программе необходимо объявить два класса:

**Ship** - для представления кораблей;

**GamePole** - для описания игрового поля.

### Класс Ship


Класс _Ship_ должен описывать корабли набором следующих параметров:

_x_, _y_ - координаты начала расположения корабля (целые числа);

_length_ - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);

_tp_ - ориентация корабля (1 - горизонтальная; 2 - вертикальная).

Объекты класса _Ship_ должны создаваться командами:

```python
ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)
```

По умолчанию (если не указывается) параметр _tp = 1_, а координаты _x_, _y_ равны _None_.

В каждом объекте класса _Ship_ должны формироваться следующие локальные атрибуты:

- _x, _y - координаты корабля (целые значения в диапазоне _[0; size)_, где _size_ - размер игрового поля);

- _length - длина корабля (число палуб);

- _tp - ориентация корабля;

- _is_move - возможно ли перемещение корабля (изначально равно _True_);

- _cells - изначально список длиной _length_, состоящий из единиц (например, при _length=3_, __cells = [1, 1, 1]_).

Список __cells_ будет сигнализировать о попадании соперником в какую-либо палубу корабля.

Если стоит 1, то попадания не было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг __is_move_ устанавливается в _False_ и перемещение корабля по игровому полю прекращается.

В самом классе _Ship_ должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

**set_start_coords(x, y)** - установка начальных координат (запись значений в локальные атрибуты _x, _y);

**get_start_coords()** - получение начальных координат корабля в виде кортежа x, y;

**move(go)** - перемещение корабля в направлении его ориентации на _go_ клеток (_go = 1_ - движение в одну сторону на клетку;
_go = -1_ - движение в другую сторону на одну клетку);

движение возможно только если флаг __is_move = True_;

**is_collide(ship)** - проверка на столкновение с другим кораблем _ship_ (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали);

метод возвращает _True_, если столкновение есть и _False_ - в противном случае;

**is_out_pole(size)** - проверка на выход корабля за пределы игрового поля (_size_ - размер игрового поля, обычно, _size = 10_);

возвращается булево значение _True_, если корабль вышел из игрового поля и _False_ - в противном случае;

С помощью магических методов **__getitem__()** и **__setitem__()** обеспечить доступ к коллекции __cells_ следующим образом:

```python
value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells
```

### Класс GamePole

Следующий класс _GamePole_ должен обеспечивать работу с игровым полем.

Объекты этого класса создаются командой:

```python
pole = GamePole(size)
```
где _size_ - размеры игрового поля (обычно, _size = 10_).

В каждом объекте этого класса должны формироваться локальные атрибуты:

**_size** - размер игрового поля (целое положительное число);

**_ships** - список из кораблей (объектов класса _Ship_); изначально пустой список.

В самом классе _GamePole_ должны быть реализованы следующие методы (возможны и другие, дополнительные методы):

**init()** - начальная инициализация игрового поля;

здесь создается список из кораблей (объектов класса _Ship_): 

- однопалубных - 4;

- двухпалубных - 3;

- трехпалубных - 2;

- четырехпалубный - 1 (ориентация этих кораблей должна быть случайной).

Корабли формируются в коллекции __ships_ следующим образом:

- однопалубных - 4;

- двухпалубных - 3;

- трехпалубных - 2;

- четырехпалубный - 1.

Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией _randint_ следующим образом:

```python
[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
```

Начальные координаты _x_, _y_ не расставленных кораблей равны _None_.

После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались между собой.

**get_ships()** - возвращает коллекцию __ships_;

**move_ships()** - перемещает каждый корабль из коллекции __ships_ на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля;

если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;

**show()** - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции __cells_ каждого корабля, вода - значением 0);

**get_pole()** - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами _size x size_ элементов.

Пример отображения игрового поля:

```
0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0
```

Пример использования классов (эти строчки в программе не писать):

```python
SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
```

В программе требуется только объявить классы _Ship_ и _GamePole_ с соответствующим функционалом. На экран выводить ничего не нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс _SeaBattle_ для управления игровым процессом в целом.
Игра должна осуществляться между человеком и компьютером.
Выстрелы со стороны компьютера можно реализовать случайным образом в свободные клетки.
Сыграйте в эту игру и выиграйте у компьютера.
