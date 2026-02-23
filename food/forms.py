from django import forms

from common.models import Allergy
from common.validators import FileSizeValidator
from food.models import Food


class FoodForm(forms.ModelForm):
    field_order = ['title', 'category', 'description', 'price', 'publishing_date', 'image', 'allergies']

    class Meta:
        model = Food
        fields = "__all__"
        exclude = ['slug']
        image = forms.ImageField(
            required=False,
            label="Drink Photo",
            validators=[FileSizeValidator(max_mb=5)]
        )

        widgets = {
            'publishing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the dish...'}),
            'allergies': forms.CheckboxSelectMultiple(),
        }




