class HandlerGET:
    """Класс-декоратор"""

    def __init__(self, func):
        self.__fn = func

    def get(self, func, request, *args, **kwargs):
        if "method" in request and request["method"] != "GET":
            return None
        else:
            return f"GET: {func(request)}"

    def __call__(self, request):
        return self.get(self.__fn, request)


@HandlerGET
def contact(request):
    return "Sergey Balakirev"


res = contact({})
print(res)


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
