from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateTaskAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTaskAPIView.as_view(), name='get_delete_update_movie'),
]