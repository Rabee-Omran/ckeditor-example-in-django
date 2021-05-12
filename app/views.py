from django.shortcuts import render
from app.forms import PostForm
from app.models import Post
# Create your views here.


def hello(request):

   
    form = PostForm(request.POST or None)
   

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'hello.html', {'form': form})


def all_posts(request):
    posts = Post.objects.all()

    return render(request, 'posts_list.html',{'posts': posts})