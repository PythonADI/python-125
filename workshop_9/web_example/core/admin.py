from django.contrib import admin
from unfold.admin import ModelAdmin
from core.models import Product, Category, ProductImage, Tag

# Register your models here.
admin.site.register([Category, Tag])


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdminModel(ModelAdmin):
    model = Product

    inlines = [ProductImageInline]
    filter_vertical = ["tags"]
    search_fields = ["name", "tags__title", "category__name"]
    list_filter = ["category__name", "tags"]
