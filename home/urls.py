from django.urls import path

from .views import index, about_page

app_name = 'home'

urlpatterns = [
    path('<str:page>/', about_page, name='about'),
    path('', index, name='index')
]

