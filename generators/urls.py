from django.urls import path

from . import views

app_name = "generators"

urlpatterns = [
    path("player-character", views.create_player_character, name="player-character"),
    path("weather-forecast", views.roll_weather_view, name="weather-forecast"),
    path("travel-hasard", views.roll_travel_hazard_view, name="travel-hazards"),
]
