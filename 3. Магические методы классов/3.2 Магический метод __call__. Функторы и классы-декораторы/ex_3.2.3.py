class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        filename = args[0]
        for ext in self.extensions:
            if ext == filename[filename.rfind(".") + 1 :]:
                return filename


filenames = [
    "boat.jpg",
    "web.png",
    "text.txt",
    "python.doc",
    "ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.png",
]
acceptor = ImageFileAcceptor(("jpg", "bmp", "jpeg"))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
