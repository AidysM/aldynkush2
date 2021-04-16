from django.urls import path

from .views import index, about_page, contact_page, AKLoginView, profile, AKLogoutView, ChangeUserInfoView
from .views import AKPasswordChangeView, RegisterUserView, RegisterDoneView, user_activate, DeleteUserView
from .views import by_rubric

app_name = 'home'

urlpatterns = [
    path('accounts/logout/', AKLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', AKPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accoutns/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', AKLoginView.as_view(), name='login'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', contact_page, name='contact'),
    path('<str:page>/', about_page, name='about'),
    path('', index, name='index'),
]

