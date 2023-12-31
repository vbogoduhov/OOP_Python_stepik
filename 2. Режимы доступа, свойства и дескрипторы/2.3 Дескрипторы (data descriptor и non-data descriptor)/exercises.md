# Дескрипторы (data descriptor и non-data descriptor)

## ex. 6
### Объявите дескриптор данных _FloatValue_, который бы устанавливал и возвращал вещественные значения. 
При записи вещественного числа должна выполняться проверка на вещественный тип данных. 
Если проверка не проходит, то генерировать исключение командой:
```python
raise TypeError("Присваивать можно только вещественный тип данных.")
```

Объявите класс _Cell_, в котором создается объект value дескриптора _FloatValue_. 
А объекты класса _Cell_ должны создаваться командой:
```python
cell = Cell(начальное значение ячейки)
```

Объявите класс _TableSheet_, с помощью которого создается таблица из _N_ строк и _M_ столбцов следующим образом:
```python
table = TableSheet(N, M)
```

Каждая ячейка этой таблицы должна быть представлена объектом класса _Cell_, 
работать с вещественными числами через объект _value_ (начальное значение должно быть 0.0).

В каждом объекте класса _TableSheet_ должен формироваться локальный атрибут:

_cells_ - список (вложенный) размером _N_ x _M_, содержащий ячейки таблицы (объекты класса _Cell_).

Создайте объект _table_ класса _TableSheet_ с размером таблицы _N = 5_, _M = 3_. 
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

## ex. 7
### Объявите класс _ValidateString_ для проверки корректности переданной строки. Объекты этого класса создаются командой:
```python
validate = ValidateString(min_length=3, max_length=100)
```

где 

_min_length_ - минимальное число символов в строке; 

_max_length_ - максимальное число символов в строке.

В классе _ValidateString_ должен быть реализован метод:

**validate(self, string)** - возвращает _True_, если _string_ является строкой (тип _str_) и длина строки в пределах _[min_length; max_length]_. 
Иначе возвращается _False_.

Объявите дескриптор данных _StringValue_ для работы со строками, объекты которого создаются командой:
```python
st = StringValue(validator=ValidateString(min_length, max_length))
```

При каждом присвоении значения объекту _st_ должен вызываться валидатор (объект класса _ValidateString_) и с помощью метода _validate()_ 
проверяться корректность присваиваемых данных. Если данные некорректны, то присвоение не выполняется (игнорируется).

Объявите класс _RegisterForm_ с тремя объектами дескриптора _StringValue_:

```python
login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.
```


Объекты класса _RegisterForm_ создаются командой:
```python
form = RegisterForm(логин, пароль, email)
```

где логин, пароль, email - начальные значения логина, пароля и Email.
В классе _RegisterForm_ также должны быть объявлены методы:

**get_fields()** - возвращает список из значений полей в порядке _[login, password, email]_;

**show()** - выводит в консоль многострочную строку в формате:
```python
<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>
```

## ex. 8
### Вы начинаете создавать интернет-магазин. 
Для этого в программе объявляется класс _SuperShop_, объекты которого создаются командой:
```python
myshop = SuperShop(название магазина)
```

В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:

_name_ - название магазина (строка);

_goods_ - список из товаров.

Также в классе _SuperShop_ должны быть методы:

**add_product(product)** - добавление товара в магазин (в конец списка _goods_);

**remove_product(product)_ - удаление товара из магазина (из списка _goods_).

Здесь _product_ - это объект класса _Product_, описывающий конкретный товар. 
В этом классе следует объявить следующие дескрипторы:

```python
name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
price = PriceValue(max_value)    # max_value - максимально допустимое значение
```

Объекты класса _Product_ будут создаваться командой:
```python
pr = Product(наименование, цена)
```

Классы _StringValue_ и _PriceValue_ - это дескрипторы данных. 
Класс _StringValue_ должен проверять, что присваивается строковый тип с длиной строки в диапазоне _[2; 50]_, 
т.е. _min_length = 2_, _max_length = 50_. 
Класс _PriceValue_ должен проверять, что присваивается вещественное или целочисленное значение в диапазоне _[0; 10000]_, 
т.е. _max_value = 10000_. Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.

Пример использования класса _SuperShop_ (эти строчки в программе писать не нужно):

```python
shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
```

## ex. 9
### Необходимо объявить класс _Bag_ (рюкзак), объекты которого будут создаваться командой:
```python
bag = Bag(max_weight)
```

где _max_weight_ - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

___things_ - список вещей в рюкзаке (изначально список пуст).

Сам же класс _Bag_ должен иметь объект-свойство:

_things_ - для доступа к локальному приватному атрибуту ___things_ (только для считывания, не записи).

Также в классе _Bag_ должны быть реализованы следующие методы:

**add_thing(self, thing)** - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (_max_weight_) не будет превышен, иначе добавление не происходит);

**remove_thing(self, indx)** - удаление предмета по индексу списка ___things_;

**get_total_weight(self)** - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса _Thing_ и создается командой:
```python
t = Thing(название, вес)
```

где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

В каждом объекте класса _Thing_ должны формироваться локальные атрибуты:

_name_ - наименование предмета;

_weight_ - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):
```python
bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
```

## ex. 10
### Необходимо написать программу для представления и управления расписанием телевизионного вещания. 
Для этого нужно объявить класс _TVProgram_, объекты которого создаются командой:
```python
pr = TVProgram(название канала)
```
где название канала - это строка с названием телеканала.

В каждом объекте класса _TVProgram_ должен формироваться локальный атрибут:

_items_ - список из телепередач (изначально список пуст).

В самом классе _TVProgram_ должны быть реализованы следующие методы:

**add_telecast(self, tl)** - добавление новой телепередачи в список _items_;

**remove_telecast(self, indx)** - удаление телепередачи по ее порядковому номеру (атрибуту ___id_, см. далее).

Каждая телепередача должна описываться классом _Telecast_, объекты которого создаются командой:
```python
tl = Telecast(порядковый номер, название, длительность)
```

где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); 
название - наименование телепередачи; 
длительность - время телепередачи (в секундах - целое число).

Соответственно, в каждом объекте класса _Telecast_ должны формироваться локальные приватные атрибуты:

___id_ - порядковый номер (целое число);

___name_ - наименование телепередачи (строка);

___duration_ - длительность телепередачи в секундах (целое число).

Для работы с этими приватными атрибутами в классе _Telecast_ должны быть объявлены соответствующие объекты-свойства (property):

**uid** - для записи и считывания из локального атрибута ___id_;

**name** - для записи и считывания из локального атрибута ___name_;

**duration** - для записи и считывания из локального атрибута ___duration_.

Пример использования классов (эти строчки в программе писать не нужно):

```python
pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
```