class Morph(object):
    """docstring for Mprph."""

    def __init__(self, *args):
        super(Morph, self).__init__()
        self.words = [word.lower() for word in args]

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return True if other.lower() in self.words else False


dict_words = [
    Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях"),
    Morph(
        "формула",
        "формулы",
        "формуле",
        "формулу",
        "формулой",
        "формул",
        "формулам",
        "формулами",
        "формулах",
    ),
    Morph(
        "вектор",
        "вектора",
        "вектору",
        "вектором",
        "векторе",
        "векторы",
        "векторов",
        "векторам",
        "векторами",
        "векторах",
    ),
    Morph(
        "эффект",
        "эффекта",
        "эффекту",
        "эффектом",
        "эффекте",
        "эффекты",
        "эффектов",
        "эффектам",
        "эффектами",
        "эффектах",
    ),
    Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях"),
]


def clear_dust(text):
    char = "–?!,.;"
    st = text
    for ch in char:
        st = st.replace(ch, "")
    return st


# text = input()
text = "Мы будем устанавливать связь завтра днем."
count = 0
for word in clear_dust(text).split():
    for morph in dict_words:
        if word == morph:
            count += 1

print(count)
