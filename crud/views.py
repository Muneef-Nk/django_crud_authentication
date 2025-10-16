from rest_framework import generics, status
from .models import Crud
from .serializers import CrudSerializer
from rest_framework.permissions import IsAuthenticated

# Create and List
class CrudListCreateView(generics.ListCreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
    permission_classes = [IsAuthenticated]


# Retrieve, Update, Delete single record
class CrudRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
    permission_classes = [IsAuthenticated]
