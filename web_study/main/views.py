from django.shortcuts import render
from .models import Post

# Create your views here.

# index.html을 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html을 부르는 blog 함수
def blog(request):
    # 모든 post를 postlist에 저장
    postlist = Post.objects.all()
    # blog 페이지를 open할 때 postlist도 함께 open
    return render(request, 'main/blog.html', {'postlist':postlist})