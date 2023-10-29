from .char_names import (
    male_first_names,
    female_first_names,
    surnames_first_part,
    surnames_last_part,
)
from .delusions import delusions
from .assets import assets
from .relationships import relationships
from .mannerisms import mannerisms
from .liabilities import liabilities
from .effects import effects
from .monster_traits import monster_traits
from .elements import elements
from .powers import powers
from .forms import forms
from .locations import locations
from .monsters import monsters
from .animals import animals
from .organs import organs
from .mutations import mutations
from .place_traits import place_traits
from .qualities import qualities
from .room_details import room_details
from .room_themes import room_themes
from .signs import signs
from .structures import structures
from .wizard_names import wizard_names
from .scents import scents
from .sounds import sounds
from .dungeons import dungeons
from .delve_shifts import delve_shifts
from .rooms import rooms
from .travel_shifts import travel_shifts
from .trap_effects import trap_effects
from .hazards import hazards
from .mechanisms import mechanisms
from .activities import activities
from .disasters import disasters
from .magic_schools import magic_schools
from .domains import domains
from .symbols import symbols
from .potions import potions
from .textures import textures
from .tastes import tastes
from .colors import colors
from .ingredients import ingredients
from .tools import tools
from .miscellaneous_items import miscellaneous_items
from .books import books
from .clothing import clothing
from .fabrics import fabrics
from .decorations import decorations
from .treasures import treasures
from .materials import materials
from .weapons import weapons
from .item_traits import item_traits
from .city_themes import city_themes
from .city_events import city_events
from .street_details import street_details
from .tactics import tactics
from .weaknesses import weaknesses
from .buildings import buildings
from .food_traits import food_traits
from .food import food
from .factions import factions
from .faction_traits import faction_traits
from .missions import missions
from .rewards import rewards
from .archetypes import archetypes
from .personalities import personalities
from .npc_details import npc_details
from .professions import professions
from .goals import goals
from .reactions import reactions

_master_table = {
    "male_first_names": male_first_names,
    "female_first_names": female_first_names,
    "surnames_first_part": surnames_first_part,
    "surnames_last_part": surnames_last_part,
    "delusions": delusions,
    "effects": effects,
    "elements": elements,
    "forms": forms,
    "locations": locations,
    "mutations": mutations,
    "place_traits": place_traits,
    "qualities": qualities,
    "rooms": rooms,
    "room_details": room_details,
    "room_themes": room_themes,
    "signs": signs,
    "structures": structures,
    "wizard_names": wizard_names,
    "dungeons": dungeons,
    "delve_shifts": delve_shifts,
    "travel_shifts": travel_shifts,
    "trap_effects": trap_effects,
    "hazards": hazards,
    "mechanisms": mechanisms,
    "activities": activities,
    "disasters": disasters,
    "magic_schools": magic_schools,
    "domains": domains,
    "symbols": symbols,
    "potions": potions,
    "textures": textures,
    "tastes": tastes,
    "colors": colors,
    "ingredients": ingredients,
    "tools": tools,
    "miscellaneous_items": miscellaneous_items,
    "books": books,
    "clothing": clothing,
    "fabrics": fabrics,
    "decorations": decorations,
    "treasures": treasures,
    "materials": materials,
    "weapons": weapons,
    "item_traits": item_traits,
    "city_themes": city_themes,
    "city_events": city_events,
    "street_details": street_details,
    "buildings": buildings,
    "food_traits": food_traits,
    "food": food,
    "factions": factions,
    "faction_traits": faction_traits,
    "missions": missions,
    "rewards": rewards,
    "archetypes": archetypes,
    "personalities": personalities,
    "npc_details": npc_details,
    "professions": professions,
    "goals": goals,
    "assets": assets,
    "liabilities": liabilities,
    "relationships": relationships,
    "reactions": reactions,
    "mannerisms": mannerisms,
    "monsters": monsters,
    "animals": animals,
    "organs": organs,
    "monster_traits": monster_traits,
    "powers": powers,
    "scents": scents,
    "sounds": sounds,
    "tactics": tactics,
    "weaknesses": weaknesses,
}
