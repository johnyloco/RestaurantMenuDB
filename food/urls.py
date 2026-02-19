from django.urls import path, include
from food import views

app_name = 'food'

food_patterns = [
    path('', views.FoodMenu.as_view(), name='food_menu'),
    path('add/', views.AddFood.as_view(), name='food_add'),
    path('<int:pk>/', include([
        path('edit/', views.EditFood.as_view(), name='edit_food' ),
        path('delete/', views.DeleteFood.as_view(), name='delete_food'),
    ])),
    path('<slug:slug>/', views.FoodDetails.as_view(), name='details_food'),

]

urlpatterns = [
    path('', views.FoodAllergies.as_view(), name='food_allergies'),
    path('foodmenu/', include(food_patterns)),
]