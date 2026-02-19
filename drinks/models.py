from django.db import models

from common.models import Allergy
from common.validators import FileSizeValidator, RangeValidator


class Drink(models.Model):
    class DrinkCategory(models.TextChoices):
        #HOT DRINKS
        COFFEE = 'COFFEE', 'Coffee'
        TEA = 'TEA', 'Tea'
        #NON ALCOHOLIC
        NONALCOHOLIC = 'NONALCOHOLIC', 'Nonalcoholic'
        MOCKTAILS = 'MOCKTAILS', 'Mocktails'
        JUICE = 'JUICE', 'Juice'
        #FERMENTED
        BEER = 'BEER', 'Beer'
        #SPIRITS
        ALCOHOLIC = 'ALCOHOLIC', 'Alcoholic'
        COCKTAIL = 'COCKTAIL', 'Cocktail'
        SPIRIT = 'SPIRIT', 'Spirit'
        #DIGESTIVES
        APERITIF = 'APERITIF', 'Aperitif'
        DIGESTIF = 'DIGESTIF', 'Digestif'
        #LIQUEURS
        LIQUEUR = 'LIQUEUR', 'Liqueur'
        #FERMENTED
        FERMENTED = 'FERMENTED', 'Fermented'
        SAKE = 'SAKE', 'Sake'

    category = models.CharField(
        max_length=50,
        choices=DrinkCategory.choices,
        default=DrinkCategory.NONALCOHOLIC
    )

    title = models.CharField(
        unique=True,
        max_length=100,
    )

    price = models.DecimalField(
        validators=[RangeValidator(
            0, 1000, message="Price must be between 0 and 100000"
        )],
        max_digits=6,
        decimal_places=2,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='drinks_images/',
        validators=[FileSizeValidator(max_mb=5)],
        null=True,
        blank=True
    )

    allergies = models.ManyToManyField(
        Allergy,
        related_name="drinks",
        blank=True
    )

    publishing_date = models.DateField()

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )


class Wine(models.Model):
    class WineCategory(models.TextChoices):
        RED = 'RED', 'Red'
        WHITE = 'WHITE', 'White'
        ROSE = 'ROSE', 'Rosé'
        SPARKLING = 'SPARK', 'Sparkling'
        FORTIFIED = 'FORT', 'Fortified'
        DESSERT = 'DESSERT', 'Dessert'

    title = models.CharField(unique=True, max_length=100)

    category = models.CharField(
        max_length=50,
        choices=WineCategory.choices,
        default=WineCategory.RED,
    )

    price = models.DecimalField(
        validators=[RangeValidator(
            0, 1000, message="Price must be between 0 and 1000")],
        max_digits=6,
        decimal_places=2,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='wines_images/',
        validators=[FileSizeValidator(max_mb=5)],
        null=True,
        blank=True
    )

    allergies = models.ManyToManyField(
        Allergy, related_name="wines", blank=True
    )
    publishing_date = models.DateField()
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"