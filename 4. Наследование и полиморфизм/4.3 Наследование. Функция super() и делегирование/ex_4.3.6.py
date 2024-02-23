class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

class Callback(object):
    """docstring for Callback."""
    def __init__(self, path, cls_route):
        self.path = path
        self.cls_route = cls_route

    def __call__(self, func):
        self.cls_route.add_callback(self.path, func)

@Callback('/about', Router)
def about():
    return '<h1>About</h1>'


route = Router.get('/about')
ret = route()
assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

route = Router.get('/')
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"
