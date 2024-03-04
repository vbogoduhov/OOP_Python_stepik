CURRENT_OS = "linux"  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory(object):
    """docstring for FileDialogFactory."""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == "windows":
            cls.__instance = cls.create_windows_filedialog(*args)
        if CURRENT_OS == "linux":
            cls.__instance = cls.create_linux_filedialog(*args)

        return cls.__instance

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


dlg = FileDialogFactory("Изображения", "d:/images/", ("jpg", "gif", "bmp", "png"))

print(type(dlg))
