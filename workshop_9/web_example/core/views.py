from django.shortcuts import render, get_object_or_404
from core.models import Product, Category
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class HomeView(ListView):
    model = Product
    paginate_by = 4
    template_name = "test.html"


class ProductView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "product_create.html"
    # success_url = "/"


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "product_create.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/"
    template_name = "product_confirm_delete.html"


def home_view(request):
    return render(
        request,
        "test.html",
        {
            "categories": Category.objects.all(),
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
