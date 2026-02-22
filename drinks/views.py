from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from drinks import models
from drinks.forms import DrinkForm, WineForm
from drinks.models import Drink, Wine


#Drinks class based views
class DrinkMenu(ListView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-menu.html'
    context_object_name = 'drinks'

class DrinkDetails(DetailView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-details.html'

class AddDrink(CreateView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-add.html'
    success_url = reverse_lazy('drinks:drink-menu')

class EditDrink(UpdateView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-edit.html'
    success_url = reverse_lazy('drinks:drink-menu')

class DeleteDrink(DeleteView):
    model = Drink
    template_name = 'drinks/all_drinks/drink-delete.html'
    success_url = reverse_lazy('drinks:drink-menu')


    #Wines class based views
class WineMenu(ListView):
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-menu.html'
    context_object_name = 'wines'

class WineDetails(DetailView):
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-details.html'

class AddWine(CreateView): # Use CreateView for adding new items
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-add.html'
    success_url = reverse_lazy('drinks:wine-menu')

class EditWine(UpdateView):
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-edit.html'
    success_url = reverse_lazy('drinks:wine-menu')

class DeleteWine(DeleteView):
    model = Wine
    template_name = 'drinks/wine/wine-delete.html'
    success_url = reverse_lazy('drinks:wine-menu')


