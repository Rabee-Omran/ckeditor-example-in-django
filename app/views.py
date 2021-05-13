from django.shortcuts import redirect, render
from app.forms import PostForm
from app.models import Post
from django.urls import reverse
from django.http.response import HttpResponseRedirect
# Create your views here.


def home(request):

   
    form = PostForm(request.POST or None)
   

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'hello.html', {'form': form})


def all_posts(request):
    posts = Post.objects.all()

    return render(request, 'posts_list.html',{'posts': posts})



def post_update(request, id ):
    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('all_posts'))


    return render(request, 'post_update.html', {'form': form})


def post_delete(request, id):
    instance = Post.objects.get(id=id)
    instance.delete()

    return redirect('all_posts')

 
