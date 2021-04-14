from django.urls import path

from .views import index, about_page, contact_page, AKLoginView, profile, AKLogoutView

app_name = 'home'

urlpatterns = [
    path('accounts/logout/', AKLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', AKLoginView.as_view(), name='login'),
    path('<str:page>/', contact_page, name='contact'),
    path('<str:page>/', about_page, name='about'),
    path('', index, name='index'),
]

