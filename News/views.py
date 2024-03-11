from django.shortcuts import render, redirect
from django.views.generic import DetailView
from News.models import Post
from News.forms import PostForm

def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-date')
    return render(request, 'home.html', {'posts': posts, 'form': form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
