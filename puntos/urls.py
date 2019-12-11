from django.urls import  path
from puntos.views import index, person_view

urlpatterns= [

    path('', views.index, name='index'),
    
]
