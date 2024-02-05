class Player(object):
    """docstring for Player."""

    def __init__(self, name, old, score):
        super(Player, self).__init__()
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return True if self.score > 0 else False


lst_in = ["Балакирев; 34; 2048", "Mediel; 27; 0", "Влад; 18; 9012", "Nina P; 33; 0"]


players = [
    Player(
        item.split(sep=";")[0], int(item.split(sep=";")[1]), int(item.split(sep=";")[2])
    )
    for item in lst_in
]

players_filtered = list(filter(bool, players))
print(players_filtered)
