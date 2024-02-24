class SoftList(list):
    """docstring for SoftList."""
    def __getitem__(self, key):
        if key < 0:
            if abs(key) > len(self):
                return False
            return super().__getitem__(key)
        else:
            if key >= len(self):
                return False
            return super().__getitem__(key)

sl = SoftList("python")
print(sl[0], sl[-1], sl[6], sl[-7])
