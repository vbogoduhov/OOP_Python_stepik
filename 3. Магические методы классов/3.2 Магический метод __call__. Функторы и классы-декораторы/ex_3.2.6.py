class RenderList:
    """Рендер и формирование HTML-тегов"""

    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        if self.type_list == "ol":
            out_string = "\n".join(
                [
                    f"<{self.type_list}>",
                    *[f"<li>{listmenu}</li>" for listmenu in args[0]],
                    f"</{self.type_list}>",
                ]
            )
        else:
            out_string = "\n".join(
                ["<ul>", *[f"<li>{listmenu}</li>" for listmenu in args[0]], "</ul>"]
            )
        return out_string


render = RenderList("ol")
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]

html = render(lst)
print(html)
