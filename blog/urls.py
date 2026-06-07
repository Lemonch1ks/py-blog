from django.urls import path

from blog.views import IndexView, post_detail

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]
