from django.urls import path, include

from . import views
from .views import index

app_name = 'core'

urlpatterns = [
    path('', index, name='core'),
    path('products/<int:catalog_id>', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('catalog/', views.catalog, name='catalog'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
]
