from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mission/',views.mission,name='mission'),
    path('vision/',views.vision,name='vision'),
    path('objectives/',views.objectives,name='objectives'),
    path('aboutproject/',views.aboutproject,name='aboutproject'),
    path('helpus/',views.helpus,name='helpus'),

]
