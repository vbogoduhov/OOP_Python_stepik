class GenericView(object):
    """docstring for GenericView."""

    def __init__(self, methods=("GET",)):
        super(GenericView, self).__init__()
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    """docstring for DetailView."""

    def __init__(self, methods=("GET",)):
        super(DetailView, self).__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError("данный запрос не может быть выполнен")
        func = getattr(self, method.lower())
        return func(request)

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError("request не является словарем")
        else:
            if "url" not in request:
                raise TypeError("request не содержит обязательного ключа url")

        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request(
    {"url": "https://site.ru/home"}, "GET"
)  # url: https://site.ru/home
print(html)
