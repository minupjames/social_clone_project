from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="all_post"),
    path('new/', views.CreatePost.as_view(), name="create"),
    path('by/<username>/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('by/<username>/', views.UserPosts.as_view(), name="user_post"),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name="delete"),
    ]