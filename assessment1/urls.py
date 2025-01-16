from django.urls import path
from assessment1.views import login,signup

urlpatterns = [
    path('',login,name='login'),
    path('signup',signup,name='signup'),
]
