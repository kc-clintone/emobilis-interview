from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Post
# from django.contrib.auth.decorators import login_required

def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(content=content, author=request.user)
        return redirect('home')
    return render(request, 'create_post.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    # Implement login logic
    pass
def logout_view(request):
    # Implement logout logic
    pass

