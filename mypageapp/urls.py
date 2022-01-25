from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mypageapp'

urlpatterns = [
    path('<int:id>/', views.home, name='home'),
    path('pet/', views.home_pet, name='home_pet'),

    path('list/', views.pet_list, name='pet_list'),
    # path('show/<int:id>/', views.show, name = 'show'),

    path('edit/', views.edit, name='edit'),
    path('profile/update/<int:id>', views.pet_profile_update, name ='pet_profile_update'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)