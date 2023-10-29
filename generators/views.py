from django.shortcuts import render
from django.views.generic import TemplateView
from random import choice
from game_logic.roll_weather import roll_weather
from game_logic.roll_travel_hazards import roll_travel_hazards
from game_logic.tables.travel_hazards import travel_hazards_table
from game_logic.tables.delve_hazards import delve_hazards_table
from game_logic.tables.weather import weather_roll_table_dict
from game_logic.characters import Character
from game_logic.roll import roll
from .forms import CharacterCreationForm
from game_logic.spells import SPELLS
from game_logic.tables._master_table import _master_table
from game_logic.tables.inn_names import inn_name_1, inn_name_2
from game_logic.npc import NPC
from game_logic.random_monster import RandomMonster
from game_logic.random_spell import get_random_spell
from game_logic.potion import Potion
from game_logic.tables.potions import potions
from game_logic.tables.food import food
from game_logic.tables.food_traits import food_traits
from game_logic.tables.domains import domains
from game_logic.tables.symbols import symbols

# Create your views here.


def create_player_character(request):
    character = Character()
    attrs = ("STR", "DEX", "CON", "WIS", "INT", "CHA")

    request.session["saved_char"] = character.spit_attributes()
    return render(
        request,
        template_name="generators/character.html",
        context={"char": character, "attrs": attrs},
    )


def create_custom_player_character(request):
    attrs = ("STR", "DEX", "CON", "WIS", "INT", "CHA")
    if request.method == "POST":
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            character = Character(**form.cleaned_data)
            request.session["saved_char"] = character.spit_attributes()

            return render(
                request,
                template_name="generators/character.html",
                context={"char": character, "attrs": attrs},
            )
    form = CharacterCreationForm()
    template_name = "generators/create_custom_character.html"
    context = {"form": form, "attrs": attrs}
    return render(request, template_name, context)


def level_up_character(request, attr):
    saved_attrs = request.session.get("saved_char")
    max_level_reached = sum(saved_attrs[:6]) == 10
    character = Character(*saved_attrs)
    if character:
        character.level_up(attr)
        attrs = ("STR", "DEX", "CON", "WIS", "INT", "CHA")
        request.session["saved_char"] = character.spit_attributes()

    return render(
        request,
        template_name="generators/character.html",
        context={
            "char": character,
            "attrs": attrs,
            "max_level_reached": max_level_reached,
        },
    )


def roll_weather_view(request):
    weather = roll_weather()
    context = {"weather": weather, "weather_table": weather_roll_table_dict}
    template_name = "generators/weather.html"
    return render(request, template_name, context)


def roll_tavern_name(request):
    template_name = "generators/inn.html"
    number = 6
    inn_names = [f"{choice(inn_name_1)} {choice(inn_name_2)}" for _ in range(number)]
    food_specialties = [f"{choice(food_traits)} {choice(food)}" for _ in range(number)]
    inns = [
        {"name": name, "food": food_specialty}
        for name, food_specialty in zip(inn_names, food_specialties)
    ]
    context = {
        "inns": inns,
        "number": number,
    }
    return render(request, template_name, context)


def roll_random_spell(request):
    number = 8
    spells = [get_random_spell() for _ in range(number)]
    template_name = "generators/random_spell.html"
    context = {
        "spells": spells,
        "number": number,
    }
    return render(request, template_name, context)


def roll_npc(request):
    npc = NPC()
    context = {
        "npc": npc,
    }
    template_name = "generators/npc.html"
    return render(request, template_name, context)


def roll_random_monster(request):
    monster = RandomMonster()
    animal = RandomMonster("animal")
    context = {"monster": monster, "animal": animal}
    template_name = "generators/random_monster.html"
    return render(request, template_name, context)


def list_tables(request):
    tables = list(_master_table.keys())
    tables.sort()
    context = {"tables_list": tables}
    template_name = "generators/list_tables.html"
    return render(request, template_name, context)


def get_table(request, table_name):
    table = _master_table.get(table_name)
    random_choice = choice(table)
    # split table in 2 50 long lists, and zip them
    table = zip(table[:50], table[50:])
    template_name = "generators/tables.html"
    context = {
        "table": table,
        "table_name": table_name.replace("_", " ").title(),
        "random_choice": random_choice,
    }
    return render(request, template_name, context)


class TravelRulesView(TemplateView):
    template_name = "generators/travel_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["travel_hazards_table"] = travel_hazards_table
        context["travel_hazard"] = roll_travel_hazards()
        return context


class AlchemyRulesView(TemplateView):
    template_name = "generators/alchemy_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        potions_table = {i: p for i, p in enumerate(potions, 1)}
        context["potions_table"] = potions_table
        context["rolled_potion"] = Potion()
        return context


class RelicMagicRulesView(TemplateView):
    template_name = "generators/relic_magic_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["symbol"] = choice(symbols)
        context["patron_name"] = choice(_master_table.get("wizard_names"))
        context["patron_goal"] = choice(_master_table.get("goals"))
        context["patron_personality"] = choice(_master_table.get("personalities"))
        context["patron_mannerism"] = choice(_master_table.get("mannerisms"))
        context["patron_domains"] = [choice(domains) for _ in range(2)]
        context["relic"] = choice(_master_table.get("miscellaneous_items"))
        context["mission"] = choice(_master_table.get("missions"))
        context["potion"] = Potion()
        context["patron_power"] = choice(_master_table.get("powers"))
        return context


class DelveRulesView(TemplateView):
    template_name = "generators/delve_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delve_hazards_table"] = delve_hazards_table
        context["delve_hazard"] = roll("1d6")
        return context


class EncountersRulesView(TemplateView):
    template_name = "generators/encounters_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activities = _master_table.get("activities")
        context["activities"] = zip(activities[:50], activities[50:])
        context["rolled_activity"] = choice(activities)
        context["reactions_table"] = _master_table.get("reactions")
        context["rolled_reaction"] = roll("2d6")
        return context


class SpellListView(TemplateView):
    template_name = "generators/spell_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spelldict"] = SPELLS
        rolled_spell_name = choice(list(SPELLS.keys()))
        rolled_spell_desc = SPELLS.get(rolled_spell_name)
        context["rolled_spell_name"] = rolled_spell_name
        context["rolled_spell_desc"] = rolled_spell_desc
        return context
