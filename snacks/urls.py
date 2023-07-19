from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', SnackListView.as_view(), name = 'snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name = 'snack_details'),
    path('create', SnackCreateView.as_view(), name = 'create_snack'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = 'update_snack'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name = 'delete_snack'),
]