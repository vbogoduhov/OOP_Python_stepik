# Обработка исключений. Блоки finally и else

## ex_4

В программе вводятся два значения в одну строчку через пробел.

Значениями могут быть числа, слова, булевы величины (_True/False_).

Необходимо прочитать эти значения из входного потока.

Если оба значения являются числами, то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк).

Результат вывести на экран (в блоке _finally_).

P.S. Реализовать программу с использованием блоков _try/except/finally_.

## ex_5
### Объявите в программе класс _Point_, объекты которого должны создаваться командами:

```python
pt = Point()
pt = Point(x, y)
```

где _x_, _y_ - произвольные числа (координаты точки). 

В каждом объекте класса _Point_ должны формироваться локальные атрибуты _x, _y с соответствующими значениями.

Если аргументы не указываются (первая команда), то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел.

Значениями могут быть числа, слова, булевы величины (_True/False_).

Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то формировать объект _pt_ командой:

```python
pt = Point(x, y)
```

Если хотя бы одно из значений не числовое, то формировать объект _pt_ командой:

```python
pt = Point()
```

Реализовать этот функционал с помощью блоков _try/except_. А в блоке _finally_ вывести на экран сообщение в формате (без кавычек):
```python
"Point: x = <значение x>, y = <значение y>"
```


## ex_7
### В практике программирования блок _else_ используют как элемент отладки программы:

в него прописывают текст программы, в котором заведомо не произойдет исключений, отлавливаемых в блоке _try_.

Выполним на практике такой пример.

Вам необходимо объявить функцию с сигнатурой:

```python
def get_loss(w1, w2, w3, w4): ...
  ```


где _w1_, _w2_, _w3_, _w4_ - любые числа.

Функция должна возвращать значение, вычисленное по формуле:

```python
y = 10 * w1 // w2 - 5 * w2 * w3 + w4
```

Здесь фрагмент вычисления _w1 // w2_ содержит потенциальную ошибку деления на ноль, поэтому его следует делать в блоке _try_.

А в блоке _else_ продолжить вычисления, где не используются операции деления.

Если происходит деление на ноль, то функция должна возвращать строку:
```python
"деление на ноль"
```


## ex_8
### Объявите класс с именем _Rect_ (прямоугольник), объекты которого создаются командой:

```python
r = Rect(x, y, width, height)
```

где _x_, _y_ - координаты верхнего левого угла (любые числа);

_width_, _height_ - ширина и высота прямоугольника (положительные числа).

Ось абсцисс (Ox) направлена вправо, ось ординат (Oy) направлена вниз.

В каждом объекте класса _Rect_ должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и соответствующими значениями.

Если переданные аргументы _x_, _y_ (не числа) и _width_, _height_ не положительные числа, то генерировать исключение командой:

```python
raise ValueError('некорректные координаты и параметры прямоугольника')
```

В классе _Rect_ реализовать метод:

```python
def is_collision(self, rect): ...
```

который проверяет пересечение текущего прямоугольника с другим (с объектом _rect_).

Если прямоугольники пересекаются, то должно генерироваться исключение командой:

```python
raise TypeError('прямоугольники пересекаются')
```

Сформировать в программе несколько объектов класса _Rect_ со следующими значениями:

```python
0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1
```


Сохранить их в списке _lst_rect_.

На основе списка _lst_rect_ сформировать еще один список _lst_not_collision_, в котором должны быть объекты _rect_ не пересекающиеся ни с какими другими объектами в списке _lst_rect_.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат (как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани второго, или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней.
