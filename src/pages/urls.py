from django.urls import path
from . import views

urlpatterns = [
    path('jupiter/', views.jupiter, name='jupiter'),
    path('earth/', views.earth, name='earth'),
    path('mercury/', views.mercury, name='mercury'),
    path('venus/', views.venus, name='venus'),
    path('mars/', views.mars, name='mars'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]