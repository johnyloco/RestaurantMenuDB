from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, ListView, DetailView

from common.models import Allergy
from food.forms import FoodForm, AllergyFilterForm
from food.models import Food




# Create your views here.
class FoodAllergies(ListView):
    model = Allergy
    form_class = FoodForm
    template_name = 'food/food-allergies.html'
    context_object_name = 'allergies'


    def get_queryset(self):
        queryset = super().get_queryset()
        # Look for 'selected_allergies' in the URL (e.g., ?selected_allergies=1&selected_allergies=2)
        allergies = self.request.GET.getlist('selected_allergies')

        if allergies:
            # We want food that does NOT have any of the selected allergies
            queryset = queryset.exclude(allergies__id__in=allergies).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the form to the template so we can see the checkboxes
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context


from django.db.models import Q


class FoodMenu(ListView):
    model = Food
    template_name = 'food/food-menu.html'
    context_object_name = 'foods'

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
        # Keep the form in the context so the checkboxes stay checked after clicking "Apply"
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context


class AddFood(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/food-add.html'
    success_url = reverse_lazy('food:food_menu')



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