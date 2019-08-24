from django.urls import path,include
from . import views

urlpatterns = [
    path('add_contact',views.add_contact,name='add_contact'),
    path('add_organization',views.add_organization,name='add_organization'),
    path('contacts',views.contacts,name='contacts'),
    path('organizations',views.organizations,name='organizations'),
    path('',views.index),
    path('contact_profile/<int:contact_id>',views.contact_profile,name='contact_profile'),
    path('organization_profile/<int:organization_id>',views.organization_profile,name='organization_profile')
]