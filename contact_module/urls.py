from django.urls import path
from . import views


urlpatterns = [
    # path('' , views.contact_us_page,name='contact_us_page'),
    path('' , views.ContactUsView.as_view(),name='contact_us_page'),
    path('create-profile/' , views.CreatProfileView.as_view(),name='create_profile_page'),
]
 

  