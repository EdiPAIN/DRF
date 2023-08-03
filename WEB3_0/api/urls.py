from django.urls import path
from .views import UserListCreateView, user_list_view, TransferViewSet

urlpatterns = [
    path('create/', UserListCreateView.as_view(), name='Create'),
    path('', user_list_view, name='user-list'),
    path('transfer/', TransferViewSet.as_view(), name='Transfer'),
]
