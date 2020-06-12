from django.urls import path

from . import views

app_name='shop'

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('', views.home, name='home'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]