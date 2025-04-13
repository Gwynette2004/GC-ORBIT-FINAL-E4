from django.urls import path
from .views import CustomUserLoginView
from .views import UserRegistrationView
from .views import ProtectedHelloView

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('hello/', ProtectedHelloView.as_view(), name='hello'),
]
