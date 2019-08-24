from django.urls import path,include
from . import views

urlpatterns = [
    path('machines',views.machines,name='machines'),
    path('spare_parts',views.spare_parts,name='spare_parts'),
    path('repaires',views.repaires,name='repaires')
]