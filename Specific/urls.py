from django.urls import path
from Specific.views import *

app_name='any'
urlpatterns=[
    path('specific1/',specific1,name='specific1'),
    path('specific2/',specific2,name='specific2'), 

    path('ram/',ram,name='ram'),
]