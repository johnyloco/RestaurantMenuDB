from common.validators import FileSizeValidator
from drinks.models import Drink, Wine
from django import forms


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = "__all__"
        exclude = ['slug']
        image = forms.ImageField(
            required=False,
            label="Drink Photo",
            validators=[FileSizeValidator(max_mb=5)]
        )
        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.CheckboxSelectMultiple(),
        }


class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = "__all__"
        exclude = ['slug', 'image_mimetype']
        image = forms.ImageField(
            required=False,
            label="Wine Photo",
            validators=[FileSizeValidator(max_mb=5)]
        )

        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.CheckboxSelectMultiple(),
        }