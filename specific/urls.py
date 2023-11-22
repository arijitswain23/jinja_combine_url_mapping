from specific.views import *
from django.urls import path
app_name='itr'

urlpatterns=[
    path('sp_iterator/',sp_iterator,name='sp_iterator'),
    path('sp_generator/',sp_generator,name='sp_generator'),
]