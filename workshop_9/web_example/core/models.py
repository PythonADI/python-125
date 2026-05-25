from django.db import models
from django.urls import reverse, reverse_lazy


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
        return reverse("product-detail", kwargs={"pk": self.pk})


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

