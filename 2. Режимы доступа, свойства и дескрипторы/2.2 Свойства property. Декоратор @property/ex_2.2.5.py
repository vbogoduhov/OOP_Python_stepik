class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_value(width):
            if width != self.__width:
                self.__width = width
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_value(height):
            if height != self.__height:
                self.__height = height
                self.show()

    def __check_value(self, value):
        return 0 <= value < 10000