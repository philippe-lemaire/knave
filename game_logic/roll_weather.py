from .tables.weather import weather_roll_table_dict as weather
from .roll import roll


def roll_weather():
    """rolls 2d6 and returns the weather associated from the weather table"""
    roll_result = roll("2d6")
    return weather.get(roll_result)
