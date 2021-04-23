from django.urls import path
from blog.views import (
                            PostListView, 
                            PostDetailView, 
                            PostCreateView, 
                            PostDeleteView, 
                            PostUpdateView
                        )


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('create/', PostCreateView.as_view(), name='post-create'),
]