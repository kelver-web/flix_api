from django.urls import path

from . import views


urlpatterns = [
    path('review/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
