from .tables.monsters import monsters
from .tables.animals import animals
from .tables.organs import organs
from .tables.monster_traits import monster_traits
from .tables.powers import powers
from .tables.scents import scents
from .tables.sounds import sounds
from .tables.tactics import tactics
from .tables.weaknesses import weaknesses
from random import choice


class RandomMonster:
    def __init__(self, type="monster"):
        self.species = choice(monsters) if type == "monster" else choice(animals)
        self.organ = choice(organs)
        self.monster_trait = choice(monster_traits)
        self.power = choice(powers)
        self.scent = choice(scents)
        self.sound = choice(sounds)
        self.tactic = choice(tactics)
        self.weakness = choice(weaknesses)
