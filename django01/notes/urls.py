from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('raw', views.raw, name='raw'),
    path('insert_post_it', views.insert_post_it, name='insert_post_it'),

]
