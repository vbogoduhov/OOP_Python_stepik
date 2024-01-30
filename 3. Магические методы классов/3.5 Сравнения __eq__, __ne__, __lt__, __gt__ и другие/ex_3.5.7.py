class FileAcceptor(object):
    """docstring for FileAcceptor."""

    def __init__(self, *args):
        super(FileAcceptor, self).__init__()
        self.lst_ext = list(args)

    def __call__(self, filename):
        for ext in self.lst_ext:
            if filename[filename.rfind(".") +1:] == ext:
                return True
        return False

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*list(set(self.lst_ext) | set(other.lst_ext)))


filenames = [
    "boat.jpg",
    "ans.web.png",
    "text.txt",
    "www.python.doc",
    "my.ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.xls",
]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
acceptor = acceptor_docs + acceptor_images
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)
