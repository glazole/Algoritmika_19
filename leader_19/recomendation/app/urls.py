from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('search/', views.search, name='search'),
    path('test/', views.test, name='test'),
    path('results/', views.results, name='results'),

]
