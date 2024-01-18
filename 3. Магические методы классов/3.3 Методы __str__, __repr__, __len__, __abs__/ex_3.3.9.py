class Ingredient(object):
    """Класс, описывающий ингредиенты"""

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe(object):
    """Класс, описывающий рецепт"""

    def __init__(self, *args):
        super(Recipe, self).__init__()
        self._lst_ings = list(args)

    def __len__(self):
        return len(self._lst_ings)

    def add_ingredient(self, ing):
        self._lst_ings.append(ing)

    def remove_ingredient(self, ing):
        self._lst_ings.remove(ing)

    def get_ingredients(self):
        return tuple(self._lst_ings)


recipe = Recipe()
ing1 = Ingredient("Соль", 1, "столовая ложка")
recipe.add_ingredient(ing1)
ing2 = Ingredient("Мука", 1, "кг")
recipe.add_ingredient(ing2)
ing3 = Ingredient("Мясо баранины", 10, "кг")
recipe.add_ingredient(ing3)
ings = recipe.get_ingredients()
print(hasattr(ing1, "name"), hasattr(ing1, "volume"), hasattr(ing1, "measure"))

n = len(recipe)  # n = 3
print(ings, n, sep="\n")
# print(ing1, ing2, ing3, sep="\n")
