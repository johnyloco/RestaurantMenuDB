from django import forms
from .models import Allergy

class AllergyForm(forms.Form):
    # Used multiple choices
    names = forms.MultipleChoiceField(
        choices=Allergy.AllergiesChoices.choices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'allergy-checkbox'}),
        label="Select Allergies you HAVE:"
    )


class AllergyFilterForm(forms.Form):
    # Used ModelMultipleChoiceField to get all allergies from the DB
    selected_allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select allergies you HAVE:"
    )