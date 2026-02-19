from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, ListView, DetailView


# Create your views here.
class FoodAllergies(TemplateView):
    template_name = 'food/food-allergies.html'
    pass


class FoodMenu(ListView):
    template_name = 'food/food-menu.html'
    pass


class AddFood(CreateView):
    template_name = 'food/food-add.html'
    pass


class EditFood(UpdateView):
    template_name = 'food/food-edit.html'
    pass


class DeleteFood(DeleteView):
    template_name = 'food/food-delete.html'
    pass


class FoodDetails(DetailView):
    template_name = 'food/food-details.html'
    pass