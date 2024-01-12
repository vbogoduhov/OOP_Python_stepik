class Handler:
    """Класс-декоратор."""

    def __init__(self, methods=("GET",)):
        self.methods = methods

    def get(self, func, request, *args, **kwargs):
        return f"{request['method']}: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"{request['method']}: {func(request)}"

    def __call__(self, func, *args, **kwargs):
        def wrapper(arg_func, *args, **kwargs):
            if len(arg_func) == 0:
                return self.get(func, {"method": "GET"})
            else:
                if ("method" in arg_func) and (arg_func["method"] not in self.methods):
                    return None
                else:
                    if arg_func["method"] == "POST":
                        return self.post(func, arg_func)
                    else:
                        return self.get(func, arg_func)

        return wrapper


@Handler(methods=("GET",))
def contact(request):
    return "Sergey Balakirev"


res = contact({})

print(res)
