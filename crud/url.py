from django.urls import path
from .views import CrudListCreateView, CrudRetrieveUpdateDeleteView

urlpatterns = [
    path('', CrudListCreateView.as_view(), name='crud-list-create'),
    path('<int:pk>/', CrudRetrieveUpdateDeleteView.as_view(), name='crud-rud'),
]
