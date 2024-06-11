from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('' , views.contact_us_page,name='contact_us_page'),
    path('' , views.ContactUsView.as_view(),name='contact_us_page'),
    path('create-profile/' , views.CreatProfileView.as_view(),name='create_profile_page'),
    path('profile/' , views.UserProfileView.as_view(),name='profile_page'),
    path('profile-list/' , views.UserProfileListView.as_view(),name='profile_list_page'),
    path('karbaran/' , views.KarbaranTestView.as_view(),name='karbaran_page'),
    path('karbaran-vorood/' , views.KarbaranVoroodView.as_view(),name='karbaran_vorood_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   