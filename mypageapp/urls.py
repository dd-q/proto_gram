from django.urls import path, include
from . import views

app_name = 'mypageapp'

urlpatterns = [
    path('<int:id>/', views.home, name='home'),
]