from django.urls import path

from . import views

app_name='video'

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<id>/',views.detailview,name='detailview'),
    path('footer/',views.footer,name='footer'),
    path('header/',views.header,name='header'),
    path('search/',views.Search,name='SearchView')
]
