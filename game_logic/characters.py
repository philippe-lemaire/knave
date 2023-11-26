from .careers import CAREERS
from .spells import SPELLS
from .metric_conversion import convert_to_metric_careers, convert_to_metric_spells
from .tables.char_names import (
    male_first_names,
    female_first_names,
    surnames_first_part,
    surnames_last_part,
)
import random

convert_to_metric_spells(SPELLS)
convert_to_metric_careers(CAREERS)


class Character:
    def __init__(
        self,
        STR=0,
        DEX=0,
        CON=0,
        INT=0,
        WIS=0,
        CHA=0,
        max_HP=0,
        gender=None,
        first_name=None,
        last_name=None,
        level=1,
        career1=None,
        career2=None,
        inventory=None,
    ):
        attributes = [int(STR), int(DEX), int(CON), int(INT), int(WIS), int(CHA)]
        if sum(attributes) == 0:
            print("rolling stats")
            rolled_attr = [random.randint(0, 5) for _ in range(3)]
            for i in rolled_attr:
                attributes[i] += 1

        self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA = attributes
        self.level = level
        genders = ("male", "female")
        if gender not in genders:
            gender = random.choice(genders)
        self.gender = gender
        self.xp = 0
        self.max_HP = max_HP
        self.set_name(first_name, last_name)
        self.update_secondary_stats()
        if career1 is None and career2 is None:
            self.careers = random.sample(sorted(CAREERS), 2)
        else:
            self.careers = [career1, career2]
        if not inventory:
            self.inventory = CAREERS.get(self.careers[0]) + CAREERS.get(self.careers[1])
            spells = random.sample(sorted(SPELLS), self.INT)
            spells = [f"Spellbook: {spell}" for spell in spells]
            if spells:
                self.inventory.extend(spells)
        else:
            self.inventory = inventory

    def set_name(self, first_name, last_name):
        if first_name and last_name:
            self.first_name = first_name
            self.last_name = last_name
        else:
            if self.gender == "male":
                first_name = random.choice(male_first_names)
            else:
                first_name = random.choice(female_first_names)
            last_name = random.choice(surnames_first_part) + random.choice(
                surnames_last_part
            )
            self.set_name(first_name, last_name)

    def update_secondary_stats(self):
        self.max_slots = self.CON + 10

        new_hp_roll = sum([random.randint(1, 6) for _ in range(self.level)])
        if new_hp_roll > self.max_HP:
            self.max_HP = new_hp_roll
        else:
            self.max_HP += 1

    def level_up(self, attrs):
        for attr in attrs:
            current_value = getattr(self, attr)
            if current_value == 10:
                raise ValueError(f"{attr} already at 10.")
            setattr(self, attr, current_value + 1)

        self.level += 1
        self.update_secondary_stats()

    def __repr__(self):
        return f"Character(STR={self.STR}, DEX={self.DEX}, CON={self.CON}, INT={self.INT}, WIS={self.WIS}, CHA={self.CHA})"

    def spit_attributes(self):
        return (
            self.STR,
            self.DEX,
            self.CON,
            self.INT,
            self.WIS,
            self.CHA,
            self.max_HP,
            self.gender,
            self.first_name,
            self.last_name,
            self.level,
            self.careers[0],
            self.careers[1],
            self.inventory,
        )
