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


def list_tables(request):
    tables = list(_master_table.keys())
    context = {"tables_list": tables}
    template_name = "generators/list_tables.html"
    return render(request, template_name, context)


def get_table(request, table_name):
    table = _master_table.get(table_name)
    # turn table into a real dict
    table = {n: desc for n, desc in enumerate(table, 1)}
    random_choice = roll(f"1d{len(table)}")
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


class DelveRulesView(TemplateView):
    template_name = "generators/delve_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delve_hazards_table"] = delve_hazards_table
        context["delve_hazard"] = roll("1d6")
        return context


class SpellListView(TemplateView):
    template_name = "generators/spell_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spelldict"] = SPELLS
        return context
