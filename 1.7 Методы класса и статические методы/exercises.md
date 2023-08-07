# Методы класса (classmethod) и статические методы (staticmethod)

- ex. 1.7.6 _В программе предполагается реализовать парсер (обработчик) строки с данными **string** в определенный выходной формат. Для этого объявлен следующий класс:_

```python
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
```

И предполагается его использовать следующим образом:

```python
res = Loader.parse_format("4, 5, -6", Factory)
```
На выходе (в переменной _res_) ожидается получать список из набора целых чисел. Например, для заданной строки, должно получиться:

```python
[4, 5, -6]
```

Для реализации этой идеи необходимо вначале программы прописать класс _Factory_ с двумя статическими методами:

**build_sequence()** - для создания пустого списка (метод возвращает пустой список);

**build_number(string)** - для преобразования строки (_string_) в целое число (метод возвращает полученное целочисленное значение).

Объявите класс с именем _Factory_, чтобы получать на выходе искомый результат.

- ex. 1.7.7 _В программе объявлен следующий класс для работы с формами ввода логин/пароль:_

```python
class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
```
Который предполагается использовать следующим образом:

```python
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
```

Необходимо прописать классы _TextInput_ и _PasswordInput_, объекты которых формируются командами:

```python
login = TextInput(name, size)
psw = PasswordInput(name, size)
```

В каждом объекте этих классов должны быть следующие локальные свойства:

**name** - название для поля (сохраняет передаваемое имя, например, _"Логин"_ или _"Пароль"_);

**size** - размер поля ввода (целое число, по умолчанию _10_).

Также классы _TextInput_ и _PasswordInput_ должны иметь метод:

**get_html(self)** - возвращает сформированную HTML-строку в формате (1-я строка для класса _TextInput_ ; 2-я - для класса _PasswordInput_):

```python
<p class='login'><имя поля>: <input type='text' size=<размер поля> />
<p class='password'><имя поля>: <input type='text' size=<размер поля> />
```

Например, для поля _login_:

```python
<p class='login'>Логин: <input type='text' size=10 />
```

Также классы _TextInput_ и _PasswordInput_ должны иметь метод класса (_@classmethod_):

**check_name(cls, name)** - для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:

- длина имени не менее 3 символов и не более 50;
- в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы

Если проверка не проходит, то генерировать исключение командой:

```python
raise ValueError("некорректное поле name")
```

Для проверки допустимых символов в каждом классе должен быть прописан атрибут _CHARS_CORRECT_:

```python
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
```

По заданию нужно объявить только классы _TextInput_ и _PasswordInput_ с соответствующим функционалом. Более ничего.
