from django.urls import path
from assessment1.views import login,signup,userhome,adminhome

urlpatterns = [
    path('',login,name='login'),
    path('signup',signup,name='signup'),
    path('userhome',userhome,name='userhome'),
    path('adminhome',adminhome,name='adminhome'),
]
