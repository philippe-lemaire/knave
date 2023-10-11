from django.urls import path

from . import views

app_name = "generators"

urlpatterns = [
    path("player-character", views.create_player_character, name="player-character"),
    path(
        "create-custom-character",
        views.create_custom_player_character,
        name="custom-player-character",
    ),
    path(
        "player-character/level-up/<str:attr>",
        views.level_up_character,
        name="level-up",
    ),
    path("weather-forecast", views.roll_weather_view, name="weather-forecast"),
    path("travel-rules", views.TravelRulesView.as_view(), name="travel-rules"),
    path("delve-rules", views.DelveRulesView.as_view(), name="delve-rules"),
    path("spells", views.SpellListView.as_view(), name="spell-list"),
]
