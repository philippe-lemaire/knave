from django.shortcuts import render
from django.views.generic import TemplateView
from game_logic.roll_weather import roll_weather
from game_logic.roll_travel_hazards import roll_travel_hazards
from game_logic.tables.travel_hazards import travel_hazards_table
from game_logic.tables.weather import weather_roll_table_dict

# Create your views here.


def create_player_character(request):
    return None


def roll_weather_view(request):
    weather = roll_weather()
    context = {"weather": weather, "weather_table": weather_roll_table_dict}
    template_name = "generators/weather.html"
    return render(request, template_name, context)


class TravelRulesView(TemplateView):
    template_name = "generators/travel_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["travel_hazards_table"] = travel_hazards_table
        context["travel_hazard"] = roll_travel_hazards()
        return context
