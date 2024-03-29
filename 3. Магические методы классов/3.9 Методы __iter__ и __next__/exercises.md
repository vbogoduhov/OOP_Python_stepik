# Методы __iter__ и __next__

## ex_5

### Объявите в программе класс _Person_, объекты которого создаются командой:

```python
p = Person(fio, job, old, salary, year_job)
```

где _fio_ - ФИО сотрудника (строка); 
_job_ - наименование должности (строка); 
_old_ - возраст (целое число); 
_salary_ - зарплата (число: целое или вещественное); 
_year_job_ - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса _Person_ автоматически должны создаваться локальные атрибуты с такими же именами: 
_fio_, _job_, _old_, _salary_, _year_job_ и соответствующими значениями.

Также с объектами класса _Person_ должны поддерживаться следующие команды:

```python
data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
```

При работе с индексами, проверить корректность значения _indx_. 

Оно должно быть целым числом в диапазоне _[0; 4]_. 
Иначе, генерировать исключение командой:

```python
raise IndexError('неверный индекс')
```

Пример использования класса (эти строчки в программе не писать):

```python
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
```

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

## ex_6
### Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков следующей структуры:

```python
lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]
```

Для этого необходимо в программе объявить класс с именем _TriangleListIterator_, объекты которого создаются командой:

```python
it = TriangleListIterator(lst)
```

где _lst_ - ссылка на перебираемый список.

Затем, с объектами класса _TriangleListIterator_ должны быть доступны следующие операции:

```python
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
```

Итератор должен перебирать элементы списка по указанной треугольной форме.
Даже если итератору на вход будет передан прямоугольная таблица (вложенный список),
то ее перебор все равно должен осуществляться по треугольнику.
Если же это невозможно (из-за структуры списка), то естественным образом должна
возникать ошибка _IndexError: index out of range_ (выход индекса за допустимый диапазон).

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

## ex_7
### Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка.

Список представляет собой двумерную таблицу из данных:

```python
lst = [[x11, x12, ..., x1N],
       [x21, x22, ..., x2N],
       ...
       [xM1, xM2, ..., xMN]
      ]
````

Для этого в программе необходимо объявить класс с именем _IterColumn_, объекты которого создаются командой:

```python
it = IterColumn(lst, column)
```

где _lst_ - ссылка на двумерный список; 

_column_ - индекс перебираемого столбца (отсчитывается от 0).

Затем, с объектами класса _IterColumn_ должны быть доступны следующие операции:

```python
it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
```

P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно.

## ex_8
### Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:

Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

**Stack** - для представления стека в целом;

**StackObj** - для представления отдельных объектов стека.

В классе _Stack_ должны быть методы:

**push_back(obj)** - для добавления нового объекта _obj_ в конец стека;

**push_front(obj)** - для добавления нового объекта _obj_ в начало стека.

В каждом объекте класса _Stack_ должен быть публичный атрибут:

_top_ - ссылка на первый объект стека (при пустом стеке _top = None_).

Объекты класса _StackObj_ создаются командой:

```python
obj = StackObj(data)
```

где _data_ - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса _StackObj_ должны быть публичные атрибуты:

_data_ - ссылка на данные объекта;

_next_ - ссылка на следующий объект стека (если его нет, то _next = None_).

Наконец, с объектами класса _Stack_ должны выполняться следующие команды:

```python
st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
```

При работе с индексами (_indx_), нужно проверять их корректность. 
Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

```python
raise IndexError('неверный индекс')
```

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

## ex_9
### В программе необходимо реализовать таблицу _TableValues_ по следующей схеме:

Каждая ячейка таблицы должна быть представлена классом _Cell_.

Объекты этого класса создаются командой:

```python
cell = Cell(data)
```

где _data_ - данные в ячейке.

В каждом объекте класса _Cell_ должен формироваться локальный приватный атрибут ___data_ с соответствующим значением.
Для работы с ним в классе _Cell_ должно быть объект-свойство (_property_):

**data** - для записи и считывания информации из атрибута ___data_.

Сам класс _TableValues_ представляет таблицу в целом, объекты которого создаются командой:

```python
table = TableValues(rows, cols, type_data)
```

где _rows_, _cols_ - число строк и столбцов таблицы; 

_type_data_ - тип данных ячейки (_int_ - по умолчанию, _float_, _list_, _str_ и т.п.).

Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса _TableValues_ должны выполняться следующие команды:

```python
table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
  ```

При попытке записать по индексам _table[row, col]_ данные другого типа (не совпадающего с атрибутом _type_data_ объекта класса _TableValues_), должно генерироваться исключение командой:

```python
raise TypeError('неверный тип присваиваемых данных')
```

При работе с индексами _row_, _col_, необходимо проверять их корректность.
Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

```python
raise IndexError('неверный индекс')
```

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

## ex_10
### Объявите класс _Matrix_ (матрица) для операций с матрицами.
Объекты этого класса должны создаваться командой:

```python
m1 = Matrix(rows, cols, fill_value)
```

где _rows_, _cols_ - число строк и столбцов матрицы;

_fill_value_ - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное).

Если в качестве аргументов передаются не числа, то генерировать исключение:

```python
raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
```

Также объекты можно создавать командой:

```python
m2 = Matrix(list2D)
```

где _list2D_ - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных).
Если список _list2D_ не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

```python
raise TypeError('список должен быть прямоугольным, состоящим из чисел')
```

Для объектов класса _Matrix_ должны выполняться следующие команды:

```python
matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
```

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

```python
raise TypeError('значения матрицы должны быть числами')
```

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

```python
raise IndexError('недопустимые значения индексов')
```

Также с объектами класса _Matrix_ должны выполняться операторы:

```python
matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
```

Во всех этих операция должна формироваться новая матрица с соответствующими значениями.

Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

```python
raise ValueError('операции возможны только с матрицами равных размеров')
```

Пример для понимания использования индексов (эти строчки в программе писать не нужно):

```python
mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
```

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
