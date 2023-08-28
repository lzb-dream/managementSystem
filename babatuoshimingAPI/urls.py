from django.urls import path
from .views.login import UserManagement
from .views.cargo import MaterielManage


urlpatterns = [
    path('login', UserManagement.as_view()),
    path('cargo_MaterielManage', MaterielManage.as_view()),
]