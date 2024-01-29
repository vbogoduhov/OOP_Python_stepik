class StringText(object):
    """Класс представляет собой одну строчку из стихотворения,
    поделенную на слова"""

    def __init__(self, lst_words):
        super(StringText, self).__init__()
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __gt__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) > len(other.lst_words)

    def __ge__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) >= len(other.lst_words)

    def __str__(self):
        return " ".join(self.lst_words)


def clear_dust(text):
    char = "–?!,.;"
    st = text
    for ch in char:
        st = st.replace(ch, "")
    return st


stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня.",
]
lst_text = [StringText(clear_dust(text).split()) for text in stich]
lst_text_sorted = sorted(lst_text, key=len, reverse=True)
lst_text_sorted = list(map(str, lst_text_sorted))

print(lst_text_sorted, sep="\n")
