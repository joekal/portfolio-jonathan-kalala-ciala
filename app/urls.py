from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route pour la racine de l'app
    path('certifications/', views.certifications, name='certifications'),
    path('projets/', views.projets, name='projets'),
    path('articles/', views.articles, name='articles'),
]
