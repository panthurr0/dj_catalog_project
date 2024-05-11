from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/view/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactsView.as_view(), name='contacts'),
]
