from django.urls import path
from . import views

urlpatterns = [
    # path('' , views.index_page, name='home_page'),
    path('' , views.HomeView.as_view(), name='home_page'),
    path('contact-us' , views.contact_page, name='contact-page'),

]
