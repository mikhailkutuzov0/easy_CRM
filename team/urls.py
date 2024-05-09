from django.urls import path

from . import views

app_name = 'team'  # Пространство имен для URL-адресов

urlpatterns = [
    path('<int:pk>/edit/', views.edit_team, name='edit-team'),
]
