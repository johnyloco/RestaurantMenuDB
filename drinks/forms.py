from drinks.models import Drink, Wine
from django import forms


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = "__all__"
        exclude = ['slug']
        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = "__all__"
        exclude = ['slug']
        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }