class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)




class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)




class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ("title", "practices", "duration"):
            pass
        else:
            object.__delattr__(self, item)

    def __setattr__(self, key, value):
        if key == "title":
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        if key in ("practices", "duration"):
            if (type(value) is not int) or (value < 0):
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
