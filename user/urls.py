from django.urls import path
from .views import userRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', userRegisterView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
