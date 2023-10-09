from django.urls import path

from . import views

app_name = "generators"

urlpatterns = [
    path("player-character", views.create_player_character, name="player-character"),
]
