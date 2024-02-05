class MailItem(object):
    """docstring for MailItem."""

    def __init__(self, mail_from, title, content):
        super(MailItem, self).__init__()
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox(object):
    """docstring for MailBox."""

    def __init__(self):
        super(MailBox, self).__init__()
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for item in lst_in:
            tmp = item.split(sep=";")
            self.inbox_list.append(MailItem(tmp[0], tmp[1], tmp[2]))


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
