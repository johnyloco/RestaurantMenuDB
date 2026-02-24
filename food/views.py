from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, ListView, DetailView

from common.models import Allergy
from food.forms import FoodForm
from food.models import Food
from common.forms import AllergyFilterForm




# Create your views here.
class FoodAllergies(ListView):
    model = Allergy
    form_class = FoodForm
    template_name = 'food/food-allergies.html'
    context_object_name = 'allergies'


    def get_queryset(self):
        queryset = super().get_queryset()
        # Looks for 'selected_allergies' in the URL (e.g., ?selected_allergies=1&selected_allergies=2)
        allergies = self.request.GET.getlist('selected_allergies')

        if allergies:
            # Showing items excepting the selected allergies
            queryset = queryset.exclude(allergies__id__in=allergies).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the form to the template so we can see the checkboxes
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context


class FoodMenu(ListView):
    model = Food
    template_name = 'food/food-menu.html'
    context_object_name = 'foods'

    # Filter for the allergies
    def get_queryset(self):
        # Start with all food
        queryset = Food.objects.all()

        # Get the list of allergy IDs from the URL (e.g., ?selected_allergies=1&selected_allergies=3)
        selected_allergies = self.request.GET.getlist('selected_allergies')

        if selected_allergies:
            # EXCLUDE any food that has an allergy present in the selected list
            # .distinct() is important to avoid duplicate results
            queryset = queryset.exclude(allergies__id__in=selected_allergies).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Keeps the form in the context so the checkboxes stay checked after clicking "Apply"
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context


class AddFood(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/food-add.html'
    success_url = reverse_lazy('food:food_menu')


    def form_valid(self, form):
        # Grab the uploaded file from the form field named 'image'
        file = self.request.FILES.get('image')
        if file:
            # Attach it to a temporary attribute for the save() method
            form.instance.uploaded_image_file = file
        return super().form_valid(form)



class EditFood(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/food-edit.html'
    success_url = reverse_lazy('food:food_menu')
    context_object_name = 'food'


class DeleteFood(DeleteView):
    model = Food
    template_name = 'food/food-delete.html'
    success_url = reverse_lazy('food:food_menu')
    context_object_name = 'food'

class FoodDetails(DetailView):
    model = Food
    form_class = FoodForm
    template_name = 'food/food-details.html'
    context_object_name = 'food'