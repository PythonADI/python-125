from django.utils import timezone

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse, reverse_lazy


def validate_product_name(value: str):
    print(value)
    if not value.isalpha():
        raise ValidationError(
            "only alphabet characters are allowed"
        )

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Unit(models.TextChoices):
        ML = "milliliter",
        L = "Liter"

    thumbnail = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    barcode = models.CharField(max_length=255)
    name = models.CharField(max_length=255, validators=[validate_product_name])
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255, choices=Unit)
    expire_at = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7)

    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

    def get_total_inventory_value(self):
        return self.quantity * self.price

    def sell(self, quantity = 1):
        self.quantity -= quantity
        self.save()

    def delete(self, using = None, keep_parents = False):
        self.deleted_at = timezone.now()
        self.save()


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

