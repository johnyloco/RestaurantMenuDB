# Here I upload the all small common apps


from django.db import models


# Allergy data
class Allergy(models.Model):
    class AllergiesChoices(models.TextChoices):
        CELERY = "CELERY", "Celery"
        GLUTEN = "GLUTEN", "Gluten"
        CRUSTACEANS = "CRUSTACEANS", "Crustaceans"
        EGGS = "EGGS", "Eggs"
        FISH = "FISH", "Fish"
        LUPINES = "LUPINES", "Lupines"
        MILK = "MILK", "Milk/Dairy"
        MUSTARD = "MUSTARD", "Mustard"
        NUTS = "NUTS", "Tree Nuts"
        PEANUTS = "PEANUTS", "Peanuts"
        SESAME = "SESAME", "Sesame"
        SOYA = "SOYA", "Soya"
        SULPHATES = "SULPHATES", "Sulphates"

    name = models.CharField(
        max_length=50,
        choices=AllergiesChoices.choices,
        unique=True
    )

    class Meta:
        verbose_name_plural = "Allergies"
        verbose_name = "Allergy"

    def __str__(self):
        # This returns the readable output label (like "Celery")
        return self.get_name_display()


# Food taste pairing
# Coming soon