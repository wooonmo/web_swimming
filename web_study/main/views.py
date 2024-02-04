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

def posting(request, pk):
    # 게시글(post) 중 pk(primary_key)를 이용해 하나의 게시글(post)을 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})