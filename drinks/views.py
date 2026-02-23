from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from common.forms import AllergyFilterForm
from drinks import models
from drinks.forms import DrinkForm, WineForm
from drinks.models import Drink, Wine


#Drinks class based views
class DrinkMenu(ListView):
    model = Drink
    template_name = 'drinks/all_drinks/drink-menu.html'
    context_object_name = 'drinks'

    def get_queryset(self):
        #Drink object
        queryset = Drink.objects.all().order_by('category')

        selected_allergies = self.request.GET.getlist('selected_allergies')

        if selected_allergies:
            queryset = queryset.exclude(allergies__id__in=selected_allergies).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initializes the form with GET data so checkboxes stay remembered
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context

class DrinkDetails(DetailView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-details.html'

class AddDrink(CreateView):
    model = Drink
    form_class = DrinkForm
    template_name = 'drinks/all_drinks/drink-add.html'
    success_url = reverse_lazy('drinks:drink-menu')

    # Important to save the photo
    def form_valid(self, form):
        # Grab the uploaded file from the form field named 'image'
        file = self.request.FILES.get('image')
        if file:
            # Attach it to a temporary attribute for the save() method
            form.instance.uploaded_image_file = file
        return super().form_valid(form)


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

    def get_queryset(self):
        #Wine object
        queryset = Wine.objects.all().order_by('category')

        selected_allergies = self.request.GET.getlist('selected_allergies')

        if selected_allergies:
            queryset = queryset.exclude(allergies__id__in=selected_allergies).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initializes the form with GET data so checkboxes stay remembered
        context['filter_form'] = AllergyFilterForm(self.request.GET)
        return context

class WineDetails(DetailView):
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-details.html'

class AddWine(CreateView): # Use CreateView for adding new items
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-add.html'
    success_url = reverse_lazy('drinks:wine-menu')

    def form_valid(self, form):
        # 1. Grab the uploaded file from the form field named 'image'
        file = self.request.FILES.get('image')
        if file:
            # 2. Attach it to a temporary attribute for the save() method
            form.instance.uploaded_image_file = file
        return super().form_valid(form)

class EditWine(UpdateView):
    model = Wine
    form_class = WineForm
    template_name = 'drinks/wine/wine-edit.html'
    success_url = reverse_lazy('drinks:wine-menu')

class DeleteWine(DeleteView):
    model = Wine
    template_name = 'drinks/wine/wine-delete.html'
    success_url = reverse_lazy('drinks:wine-menu')


