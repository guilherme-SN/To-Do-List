from django import views
from django.urls import path
from . import views


# main app urls
urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('updateItem/<int:id_td>/<int:id_item>/', views.updateItem, name='updateItem'),
    path('updateList/<int:id_td>/', views.updateList, name='updateList')
]