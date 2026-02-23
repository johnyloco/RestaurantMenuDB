from django.urls import path, include
from drinks import views

app_name = 'drinks'

# Patterns for All kind of Drinks except wine (Coffee, Tea, Spirits, etc.)
drink_patterns = [
    path('', views.DrinkMenu.as_view(), name='drink-menu'),
    path('add/', views.AddDrink.as_view(), name='drink-add'),
    path('<int:pk>/', include([
        path('', views.DrinkDetails.as_view(), name='drink-details'),
        path('edit/', views.EditDrink.as_view(), name='drink-edit'),
        path('delete/', views.DeleteDrink.as_view(), name='drink-delete'),
    ])),
]

# Patterns for Wine
wine_patterns = [
    path('', views.WineMenu.as_view(), name='wine-menu'),
    path('add/', views.AddWine.as_view(), name='wine-add'),
    path('<int:pk>/', include([
    path('', views.WineDetails.as_view(), name='wine-details'),
        path('edit/', views.EditWine.as_view(), name='wine-edit'),
        path('delete/', views.DeleteWine.as_view(), name='wine-delete'),
    ])),
]

urlpatterns = [
    path('drink/', include(drink_patterns)),
    path('wine/', include(wine_patterns)),
]
