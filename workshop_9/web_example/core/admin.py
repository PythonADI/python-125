from django.contrib import admin
from core.models import Product, Category, ProductImage, Tag

# Register your models here.
admin.site.register([Category, Tag])


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    model = Product

    inlines = [ProductImageInline]
    filter_horizontal = ["tags"]
