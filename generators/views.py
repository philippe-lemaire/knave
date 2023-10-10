from django.shortcuts import render
from game_logic.roll_weather import roll_weather
from game_logic.roll_travel_hazards import roll_travel_hazards

# Create your views here.


def create_player_character(request):
    return None


def roll_weather_view(request):
    weather = roll_weather()
    context = {"weather": weather}
    template_name = "generators/weather.html"
    return render(request, template_name, context)


def roll_travel_hazard_view(request):
    travel_hazard = roll_travel_hazards()
    context = {"travel_hazard": travel_hazard}
    template_name = "generators/travel_hazard.html"
    return render(request, template_name, context)
