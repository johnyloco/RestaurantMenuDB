from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from common.models import Allergy
from common.validators import FileSizeValidator
from common.validators import RangeValidator




class Food(models.Model):
    class FoodTypeChoices(models.TextChoices):
        STARTER = 'STARTER', 'Starter'
        MAIN = 'MAIN', 'Main'
        DESSERT = 'DESSERT', 'Dessert'
        SNACKS = 'snacks', 'Snacks'

    category = models.CharField(
        max_length=50,
        choices=FoodTypeChoices,
        default=FoodTypeChoices.SNACKS
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
        upload_to='food_images/',
        validators=[FileSizeValidator(max_mb=5)],
        null=True,
        blank=True
    )

    allergies = models.ManyToManyField(
        Allergy,
        related_name="foods",
        blank=True
    )

    publishing_date = models.DateField()

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}")

        super().save(*args, **kwargs)