from django.urls import path

from blog.views import IndexView, post_detail

app_name = "blog"

urlpatterns = [
    path("post/", IndexView.as_view(), name="index"),
    path("post/<int:pk>", post_detail, name="post-detail"),
]
