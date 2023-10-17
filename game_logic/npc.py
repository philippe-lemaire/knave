from .tables.char_names import (
    male_first_names,
    female_first_names,
    surnames_first_part,
    surnames_last_part,
)
from .tables.personalities import personalities
from .tables.npc_details import npc_details
from .tables.professions import professions
from .tables.goals import goals
from .tables.assets import assets
from .tables.liabilities import liabilities
from .tables.relationships import relationships
from .tables.mannerisms import mannerisms
import random


class NPC:
    def __init__(self):
        self.gender = random.choice(["Male", "Female"])
        self.personality = random.choice(personalities)
        self.detail = random.choice(npc_details)
        self.profession = random.choice(professions)
        self.goal = random.choice(goals)
        self.asset = random.choice(assets)
        self.liability = random.choice(liabilities)
        self.relationship = random.choice(relationships)
        self.mannerism = random.choice(mannerisms)
        self.set_name()

    def set_name(self):
        if self.gender == "Male":
            self.first_name = random.choice(male_first_names)
        else:
            self.first_name = random.choice(female_first_names)
        first = random.choice(surnames_first_part)
        last = random.choice(surnames_last_part)
        self.last_name = first + last
