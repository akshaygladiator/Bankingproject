from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('Home',views.Home,name='Home' ),
    path('Form',views.Form,name='Form'),
    path('logout',views.logout,name='logout'),
    path('Newpage',views.Newpage,name='Newpage')
]
