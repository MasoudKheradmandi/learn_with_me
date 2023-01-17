from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.Login,name='login'),
    path('register/',views.SignUp,name='register')
]

