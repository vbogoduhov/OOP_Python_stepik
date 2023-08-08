class Viber:
    lst_msg = {}
    lst_count_msg = {}

    @classmethod
    def add_message(cls, msg):
        cls.lst_msg[msg.text] = msg
        cls.lst_count_msg[len(cls.lst_msg) + 1] = msg.text

    @classmethod
    def remove_message(cls, msg):
        cls.lst_msg.pop(msg.text)

    @classmethod
    def set_like(cls, msg):
        cls.lst_msg[msg.text].fl_like = not cls.lst_msg[msg.text].fl_like

    @classmethod
    def show_last_message(cls, number):
        lst_key = sorted(list(cls.lst_count_msg.keys()), reverse=True)
        for ind in lst_key[:number]:
            key = cls.lst_count_msg[ind]
            print(cls.lst_msg[key])

    @classmethod
    def total_messages(cls):
        return len(cls.lst_msg)
class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False