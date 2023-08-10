class AppStore:

    def __init__(self):
        self.lst_app = {}
    def add_application(self, app):
        self.lst_app[app.name] = app


    def remove_application(self, app):
        self.lst_app.pop(app.name)


    def block_application(self, app):
        app.block()


    def total_apps(self):
        return len(self.lst_app)

class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = False

    def block(self):
        self.blocked = True


