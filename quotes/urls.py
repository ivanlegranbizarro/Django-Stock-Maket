from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('add-stock', views.add_stock, name='add_stock'),
    path('delete-stock/<stock_id>', views.delete_stock, name='delete_stock')
]
