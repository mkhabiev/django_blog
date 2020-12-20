from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from posts.forms import PostForm
from posts.models import Post

@csrf_exempt
def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        post = Post.objects.create(title="Good Morning", description="Have a good day")
        return HttpResponse('Put the information to my posts')
    if method_post == 'GET':
        saved_posts = Post.objects.all()
        return HttpResponse(saved_posts)
    if method_post == 'DELETE':
        post = Post.objects.get(pk=1)
        post.delete()
        return HttpResponse('Post deleted')
    if method_post in ['PUT', 'PATCH']:
        post = Post.objects.create(title='Good Morning', description='Have a good day')
        post.title = "Good evening"
        post.description = "Good night"
        post.save()

    return HttpResponse('Hi master, i\'m working!')



class PostsView(ListView):
    model = Post
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


def add_post(request):
    method = request.method
    if method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form.data)
        Post.objects.create(title=form.data['title'],
                            description=form.data['description'],
                            image=form.data['image'],
                            text=form.data['text'])
        return HttpResponse('Post Created')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})