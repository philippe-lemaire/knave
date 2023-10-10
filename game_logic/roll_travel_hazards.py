from .roll import roll
from .tables.travel_shifts import travel_shifts
from .tables.travel_hazards import travel_hazards_table


def roll_travel_hazards():
    """rolls a travel hazard"""
    die_result = roll("1d6")
    return travel_hazards_table[die_result]
