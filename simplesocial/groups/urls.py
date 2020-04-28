from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    
    path('',views.ListGroups.as_view(),name="list_all"),
    path('posts/in/<slug>/',views.GroupDetail.as_view(),name="group_detail"),
    path('new/',views.CreateGroup.as_view(),name="create"),
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
    
 ]
