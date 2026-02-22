from django import forms

from common.models import Allergy
from food.models import Food


class FoodForm(forms.ModelForm):
    field_order = ['title', 'category', 'description', 'price', 'publishing_date', 'image', 'allergies']

    class Meta:
        model = Food
        fields = "__all__"
        exclude = ['slug']

        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the dish...'}),
        }

class AllergyFilterForm(forms.Form):
    # We use ModelMultipleChoiceField to get all allergies from the DB
    selected_allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select allergies you HAVE:"
    )


