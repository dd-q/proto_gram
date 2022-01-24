from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mypageapp'

urlpatterns = [
    path('<int:id>/', views.home, name='home'),
    path('pet/', views.home_pet, name='home_pet'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)