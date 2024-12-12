# accounts/urls.py
from django.contrib.auth.views import LoginView
from django.urls import include, path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # noqa E501
]
