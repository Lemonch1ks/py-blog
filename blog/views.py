from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comments = Commentary.objects.filter(
        post=post).select_related("user").order_by("-created_time")

    if request.method == "POST":
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.is_valid()
            form.add_error(
                None,
                "Only authorized users can post comments.",
            )
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return redirect(
                "blog:post-detail",
                pk=post.pk,
            )
    else:
        form = CommentaryForm()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context=context)
