from random import choice, randint
from .tables.wizard_names import wizard_names
from .tables.elements import elements
from .tables.forms import forms
from .tables.qualities import qualities
from .tables.forms import forms
from .tables.effects import effects


SPELL_FORMULAE = {
    1: lambda element, form, effect, quality, wizard_name: f"{element} {form}",
    2: lambda element, form, effect, quality, wizard_name: f"{effect} {form}",
    3: lambda element, form, effect, quality, wizard_name: f"{effect} {element}",
    4: lambda element, form, effect, quality, wizard_name: f"The {quality} {element} {form}",
    5: lambda element, form, effect, quality, wizard_name: f"The {quality} {effect} {form}",
    6: lambda element, form, effect, quality, wizard_name: f"The {quality} {effect} {element}",
    7: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {element} {form}",
    8: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {effect} {form}",
    9: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {effect} {element}",
    10: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {quality} {element} {form}",
    11: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {quality} {effect} {form}",
    12: lambda element, form, effect, quality, wizard_name: f"{wizard_name}’s {quality} {effect} {element}",
}


def get_random_spell():
    """Builds and returns a random spell"""
    d12 = randint(1, 12)
    element = choice(elements)
    form = choice(forms)
    effect = choice(effects)
    quality = choice(qualities)
    wizard_name = choice(wizard_names)
    formula = SPELL_FORMULAE[d12]
    spell = formula(element, form, effect, quality, wizard_name)
    return spell
