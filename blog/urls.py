from django.urls import path

from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.AddCommentView.as_view(), name='add_comment'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('', views.PostListView.as_view(), name='post_list'),
]
