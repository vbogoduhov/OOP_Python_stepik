class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get("url")


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get("url")


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get("url")


class GeneralView(object):
    """docstring for GeneralView."""

    allowed_methods = ("GET", "POST", "PUT", "DELETE")

    def __init__(self):
        super(GeneralView, self).__init__()

    def render_request(self, request):
        if not request["method"] in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get("method").lower()  # имя метода, малыми буквами
        return self.__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = (
        "GET",
        "POST",
    )

