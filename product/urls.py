from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.product_list, name="all_products"),
    path("/<id>", views.product_detail, name="product_detail"),
]