from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from common.forms import AllergyForm
from common.models import Allergy


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {"message": "Welcome to the Restaurant!"}
    return render(request, 'common/home.html', context)


def add_allergy(request):
    if request.method == "POST":
        form = AllergyForm(request.POST)
        if form.is_valid():
            selected_allergies = form.cleaned_data.get('names')

            for allergy_code in selected_allergies:
                # This manually creates the database record if it doesn't exist
                Allergy.objects.get_or_create(name=allergy_code)

            return redirect('common:home')  # Change this to your success URL
    else:
        form = AllergyForm()

    return render(request, 'common/add_allergy.html', {'form': form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)