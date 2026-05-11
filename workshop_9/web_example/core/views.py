from django.shortcuts import render, get_object_or_404
from core.models import Product


def home_view(request):
    return render(
        request,
        "test.html",
        {
            "products": Product.objects.all()
        }
    )


def product_view(request, pk):
    return render(
        request,
        "product_detail.html",
        {
            "pk": pk,
            "product": get_object_or_404(Product, pk=pk)
        })
