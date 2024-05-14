from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index_pade, name='product-list'),
]