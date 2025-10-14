from rest_framework import generics
from .models import Crud
from .serializers import CrudSerializer

# Create and List
class CrudListCreateView(generics.ListCreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

# Retrieve, Update, Delete single record
class CrudRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
