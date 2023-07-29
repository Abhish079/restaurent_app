from django.urls import path
from rlist import views
from django.contrib import admin

urlpatterns = [
    path('restaurent',views.show, name="restaurent"),
    path('restaurent/addnew',views.homepage),
    path('send',views.send),
    path('delete',views.delete),
    path('update',views.update),   
    path('restaurent/details/1',views.details),
    path('recordupdated',views.recordupdated),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('cp/',views. change_password,name='change_password'),
    path('fp/',views. forgotpassword,name='forgot_password'),
]
