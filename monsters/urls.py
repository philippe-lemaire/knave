from django.urls import path

from . import views

app_name = "monsters"

urlpatterns = [
    path("", views.MonsterListView.as_view(), name="monster_list"),
    path(
        "<int:pk>",
        views.MonsterDetailView.as_view(),
        name="detail",
    ),
]
