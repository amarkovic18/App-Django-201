from django.urls import path
from . import views 
app_name="feed"

urlpatterns=[
    path("", views.HomePageView.as_view(), name="home"),
    path("<int:pk>/",views.PostDetailView.as_view(), name="detail"),
    path("new_post/", views.CreateNewPost.as_view(), name="new_post"),
]