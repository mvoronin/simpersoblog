from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('<slug:ctg_slug>/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('<slug:ctg_slug>/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-update'),
    path('<slug:ctg_slug>/<int:pk>/publish', views.PostPublishView.as_view(), name='post-publish'),
    path('<slug:ctg_slug>/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]
