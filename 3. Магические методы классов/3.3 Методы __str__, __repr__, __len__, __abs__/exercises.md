# Методы __str__, __repr__, __len__, __abs__
## ex_2
### Объявите класс с именем _Book_ (книга), объекты которого создаются командой:

```python
book = Book(title, author, pages)
```

где: 

_title_ - название книги (строка); 

_author_ - автор книги (строка); 

_pages_ - число страниц в книге (целое число).

Также при выводе информации об объекте на экран командой:

```python
print(book)
```

должна отображаться строчка в формате:

```
"Книга: {title}; {author}; {pages}"
```

Например:

```python
"Книга: Муму; Тургенев; 123"
```

Прочитайте из входного потока строки с информацией по книге командой:

```python
lst_in = list(map(str.strip, sys.stdin.readlines()))
```
(строки идут в порядке: _title_, _author_, _pages_). 
Создайте объект класса _Book_ и выведите его строковое представление в консоль.

## ex_3
### Объявите класс с именем _Model_, объекты которого создаются командой:

```python
model = Model()
```

Объявите в этом классе метод _query()_ для формирования записи базы данных. 
Использоваться этот метод должен следующим образом:

```python
model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)
```

Например:

```python
model.query(id=1, fio='Sergey', old=33)
```

Все эти переданные данные должны сохраняться внутри объекта _model_ класса _Model_. 
Затем, при выполнении команды:

```python
print(model)
```

В консоль должна выводиться информация об объекте в формате:

```python
"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"
```

Например:

```python
"Model: id = 1, fio = Sergey, old = 33"
```

Если метод _query()_ не вызывался, то в консоль выводится строка:

```python
"Model"
```

P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.

## ex_4
### Объявите класс _WordString_, объекты которого создаются командами:

```python
w1 = WordString()
w2 = WordString(string)
```

где _string_ - передаваемая строка. Например:

```python
words = WordString("Курс по Python ООП")
```

Реализовать следующий функционал для объектов этого класса:

**len(words)** - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);

**words(indx)** - должно возвращаться слово по его индексу (_indx_ - порядковый номер слова в строке, начиная с 0).

Также в классе _WordString_ реализовать объект-свойство (property):

_string_ - для передачи и считывания строки.

Пример пользования классом _WordString_ (эти строчки в программе писать не нужно):

```python
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
```

P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.

## ex_5
### Объявите класс _LinkedList_ (связный список) для работы со следующей структурой данных:

Здесь создается список из связанных между собой объектов класса _ObjList_.
Объекты этого класса создаются командой:

```python
obj = ObjList(data)
```
где _data_ - строка с некоторой информацией. 
Также в каждом объекте _obj_ класса _ObjList_ должны создаваться следующие локальные атрибуты:

**___data - ссылка на строку с данными;

**___prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);

**___next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса _LinkedList_ должны создаваться командой:

```python
linked_lst = LinkedList()
```

и содержать локальные атрибуты:

_head_ - ссылка на первый объект связного списка (если список пуст, то head = None);

_tail_ - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

**add_obj(obj)** - добавление нового объекта _obj_ класса _ObjList_ в конец связного списка;

**remove_obj(indx)** - удаление объекта класса _ObjList_ из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса _LinkedList_ должны поддерживаться следующие операции:

**len(linked_lst)** - возвращает число объектов в связном списке;

**linked_lst(indx)** - возвращает строку ___data, хранящуюся в объекте класса _ObjList_, расположенного под индексом _indx_ (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

```python
linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
```

PS. На экран в программе ничего выводить не нужно.

## ex_6
### Объявите класс с именем _Complex_ для представления и работы с комплексными числами. 
Объекты этого класса должны создаваться командой:

```python
cm = Complex(real, img)
```

где:

_real_ - действительная часть комплексного числа (целое или вещественное значение); 

_img_ - мнимая часть комплексного числа (целое или вещественное значение).

Объявите в этом классе следующие объекты-свойства (property):

_real_ - для записи и считывания действительного значения;

_img_ - для записи и считывания мнимого значения.

При записи новых значений необходимо проверять тип передаваемых данных.
Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:

```python
raise ValueError("Неверный тип данных.")
```

Также с объектами класса _Complex_ должна поддерживаться функция:

```python
res = abs(cm)
```

возвращающая модуль комплексного числа (вычисляется по формуле: _sqrt(real*real + img*img)_ - корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).

Создайте объект cmp класса _Complex_ для комплексного числа с _real = 7_ и _img = 8_. 
Затем, через объекты-свойства _real_ и _img_ измените эти значения на _real = 3_ и _img = 4_. 
Вычислите модуль полученного комплексного числа (сохраните результат в переменной _c_abs_).

P.S. На экран ничего выводить не нужно.

## ex_7
### Объявите класс с именем _RadiusVector_ для описания и работы с n-мерным вектором (у которого n координат). 
Объекты этого класса должны создаваться командами:

```python
# создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
vector = RadiusVector(1, -5, 3.4, 10)
```

То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора.
Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.

Класс _RadiusVector_ должен содержать методы:

**set_coords(coord_1, coord_2, ..., coord_N)** - для изменения координат радиус-вектора;

**get_coords()** - для получения текущих координат радиус-вектора (в виде кортежа).

Также с объектами класса _RadiusVector_ должны поддерживаться следующие функции:

**len(vector)** - возвращает число координат радиус-вектора (его размерность);

**abs(vector)** - возвращает длину радиус-вектора (вычисляется как: _sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N)_ - корень квадратный из суммы квадратов координат).

Пример использования класса _RadiusVector_ (эти строчки в программе писать не нужно):

```python
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
```

P.S. На экран ничего выводить не нужно, только объявить класс _RadiusVector_.

## ex_8
### Объявите класс _DeltaClock_ для вычисления разницы времен. 
Объекты этого класса должны создаваться командой:

```python
dt = DeltaClock(clock1, clock2)
```

где _clock1_, _clock2_ - объекты другого класса _Clock_ для хранения текущего времени. 
Эти объекты должны создаваться командой:

```python
clock = Clock(hours, minutes, seconds)
```

где _hours_, _minutes_, _seconds_ - часы, минуты, секунды (целые неотрицательные числа).

В классе _Clock_ также должен быть (по крайней мере) один метод (возможны и другие):

**get_time()** - возвращает текущее время в секундах (то есть, значение _hours * 3600 + minutes * 60 + seconds_).

После создания объекта _dt_ класса _DeltaClock_, с ним должны выполняться команды:

```python
str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
```

Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

```python
dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
```

Обратите внимание, добавляется незначащий ноль, если число меньше 10.

P.S. На экран ничего выводить не нужно, только объявить классы.

## ex_9
### Объявите класс _Recipe_ для представления рецептов.

Отдельные ингредиенты рецепта должны определяться классом _Ingredient_. 
Объекты этих классов должны создаваться командами:

```python
ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N)
```

где _ing_1_, _ing_2_,..., _ing_N_ - объекты класса _Ingredient_.

В каждом объекте класса _Ingredient_ должны создаваться локальные атрибуты:

_name_ - название ингредиента (строка);

_volume_ - объем ингредиента в рецепте (вещественное число);

_measure_ - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

С объектами класса _Ingredient_ должна работать функция:

```python
str(ing)  # название: объем, ед. изм.
```

и возвращать строковое представление объекта в формате:

```
"название: объем, ед. изм."
```


Например:

```python
ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка
```

Класс _Recipe_ должен иметь следующие методы:

**add_ingredient(ing)** - добавление нового ингредиента _ing_ (объект класса _Ingredient_) в рецепт (в конец);

**remove_ingredient(ing)** - удаление ингредиента по объекту _ing_ (объект класса _Ingredient_) из рецепта;

**get_ingredients()** - получение кортежа из объектов класса _Ingredient_ текущего рецепта.

Также с объектами класса _Recipe_ должна поддерживаться функция:

**len(recipe)** - возвращает число ингредиентов в рецепте.

Пример использования классов (эти строчки в программе писать не нужно):

```python
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
```

P.S. На экран ничего выводить не нужно, только объявить классы.

## ex_10
### Объявите класс _PolyLine_ (полилиния) для представления линии из последовательности прямолинейных сегментов.
Объекты этого класса должны создаваться командой:

```python
poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
```

Здесь:
_start_coord_ - координата начала полилинии (кортеж из двух чисел _x_, _y_); 

_coord_2_, _coord_3_, ... - последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.

Например:

```python
ppoly = PolyLine(start_coord, coord_2, coord_3, ..., coord_Noly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
```

В классе _PolyLine_ должны быть объявлены следующие методы:

**add_coord(x, y)** - добавление новой координаты (в конец);

**remove_coord(indx)** - удаление координаты по индексу (порядковому номеру, начинается с нуля);

**get_coords()** - получение списка координат (в виде списка из кортежей).

P.S. На экран ничего выводить не нужно, только объявить класс.
