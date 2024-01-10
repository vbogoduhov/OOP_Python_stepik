# Магический метод __call__. Функторы и классы-декораторы
## ex_2

### Объявите класс _RandomPassword_ для генерации случайных паролей.
Объекты этого класса должны создаваться командой:

```python
rnd = RandomPassword(psw_chars, min_length, max_length)
```

где _psw_chars_ - строка из разрешенных в пароле символов; _min_length_, _max_length_ - минимальная и максимальная длина генерируемых паролей.

Непосредственная генерация одного пароля должна выполняться командой:

```python
psw = rnd()
```

где _psw_ - ссылка на строку длиной в диапазоне _[min_length; max_length]_ 
из случайно выбранных символов строки _psw_chars_.

С помощью генератора списка _(list comprehension)_ создайте список _lst_pass_ из трех сгенерированных паролей объектом _rnd_ класса _RandomPassword_, созданного с параметрами: 
```python
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
```
## ex_3
### Для последовательной обработки файлов из некоторого списка, например:

```python
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
```

Необходимо объявить класс _ImageFileAcceptor_, который бы выделял только файлы с указанными расширениями.

Для этого предполагается создавать объекты класса командой:

```python
acceptor = ImageFileAcceptor(extensions)
```

где _extensions_ - кортеж с допустимыми расширениями файлов, например: _extensions = ('jpg', 'bmp', 'jpeg')_.

А, затем, использовать объект _acceptor_ в стандартной функции _filter_ языка _Python_ следующим образом:

```python
image_filenames = filter(acceptor, filenames)
```

Пример использования класса (эти строчки в программе писать не нужно):
```python
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
```
## ex_4
### Предположим, мы разрабатываем класс для обработки формы авторизации на стороне сервера. 

Для этого был создан следующий класс с именем _LoginForm_:

```python
class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True
```

Здесь _name_ - это заголовок формы (строка); _validators_ - список из валидаторов для проверки корректности поля. 
В методе _post_ параметр _request_ - это словарь с ключами _'login'_ и _'password'_ и значениями (строками) для логина и пароля соответственно.

Пример использования класса _LoginForm_ (в программе не писать):

```python
from string import ascii_lowercase, digits

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
```

Вам необходимо в программе объявить классы валидаторов:

_LengthValidator_ - для проверки длины данных в диапазоне _[min_length; max_length]_;

_CharsValidator_ - для проверки допустимых символов в строке.

Объекты этих классов должны создаваться командами:

```python
lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(chars) # chars - строка из допустимых символов
```

Для проверки корректности данных каждый валидатор должен вызываться как функция:

```python
res = lv(string)
res = cv(string)
```

и возвращать _True_, если _string_ удовлетворяет условиям валидатора и _False_ - в противном случае.

## ex_5
### Объявите класс _DigitRetrieve_ для преобразования данных из строки в числа. 

Объекты этого класса создаются командой:

```python
dg = DigitRetrieve()
```

Затем, их предполагается использовать, например следующим образом:

```python
d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)
```

То есть, целые числа в строке следует приводить к целочисленному типу данных, а все остальные - к значению _None_.

С помощью объектов класса _DigitRetrieve_ должно выполняться преобразование чисел из списка строк следующим образом:
```python
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
```

## ex_6
### Предположим, вам необходимо создать программу по преобразованию списка строк, например:

```python
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
```

в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):

```html
<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>
```
Для этого необходимо объявить класс _RenderList_, объекты которого создаются командой:

```python
render = RenderList(type_list)
```

где _type_list_ - тип списка (принимает значения: _"ul"_ - для списка с тегом _<ul>_ и _"ol"_ - для списка с тегом _<ol>_). 
Если значение параметра _type_list_ другое (не _"ul"_ и не _"ol"_), то формируется список с тегом _<ul>_.

Затем, предполагается использовать объект _render_ следующим образом:

```python
html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
```

Пример использования класса (эти строчки в программе писать не нужно):
```python
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
```

