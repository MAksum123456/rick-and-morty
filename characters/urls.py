from django.urls import path

from characters.views import get_random_characters, CharacterLstView

app_name = "characters"
urlpatterns = [
    path("characters/random/", get_random_characters, name="character-random"),
    path("characters/", CharacterLstView.as_view(), name="character-list"),
]
