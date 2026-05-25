from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
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
    paginate_by = 100
    template_name = "home.html"

    def get_queryset(self):
        return super().get_queryset().select_related("category")


class ProductView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "product_create.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"{self.object.name} was successfully created!")
        return reverse("product-detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "product_create.html"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("product-list")

