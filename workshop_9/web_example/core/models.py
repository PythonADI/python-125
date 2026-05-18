from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Unit(models.TextChoices):
        ML = "milliliter",
        L = "Liter"


    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    barcode = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255, choices=Unit)
    expire_at = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.pk}/"


