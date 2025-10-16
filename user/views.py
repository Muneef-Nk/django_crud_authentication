from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import User 
# Create your views here.
class userRegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer

