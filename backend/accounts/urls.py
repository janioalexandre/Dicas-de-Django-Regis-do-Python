# accounts/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from .views import logout_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # noqa E501
    path('logout/', logout_view, name='logout'),  # noqa E501
]
