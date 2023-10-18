from .tables.potions import potions as names
from .tables.textures import textures
from .tables.tastes import tastes
from .tables.colors import colors
from .tables.ingredients import ingredients
from random import choice


class Potion:
    def __init__(self) -> None:
        self.name = f"Potion of {choice(names)}"
        self.texture = choice(textures)
        self.taste = choice(tastes)
        self.color = choice(colors)
        self.ingredient = choice(ingredients)
