"""
URL configuration for web_example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import (
    HomeView,
    ProductView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="product-list"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('products/<int:pk>/', ProductView.as_view(), name="product-detail"),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name="product-edit"),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name="product-delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

