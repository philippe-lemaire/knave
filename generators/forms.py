from django import forms
from game_logic.careers import CAREERS


class CharacterCreationForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    STR = forms.IntegerField(min_value=0, max_value=3, initial=0)
    DEX = forms.IntegerField(min_value=0, max_value=3, initial=0)
    CON = forms.IntegerField(min_value=0, max_value=3, initial=0)
    WIS = forms.IntegerField(min_value=0, max_value=3, initial=0)
    INT = forms.IntegerField(min_value=0, max_value=3, initial=0)
    CHA = forms.IntegerField(min_value=0, max_value=3, initial=0)
    career_choices = sorted([(name, name) for name in CAREERS.keys()])
    career1 = forms.ChoiceField(choices=career_choices)
    career2 = forms.ChoiceField(choices=career_choices)


class LevelUpForm(forms.Form):
    STR = forms.BooleanField(label="Raise STR", required=False)
    DEX = forms.BooleanField(label="Raise DEX", required=False)
    CON = forms.BooleanField(label="Raise CON", required=False)
    WIS = forms.BooleanField(label="Raise WIS", required=False)
    INT = forms.BooleanField(label="Raise INT", required=False)
    CHA = forms.BooleanField(label="Raise CHA", required=False)
