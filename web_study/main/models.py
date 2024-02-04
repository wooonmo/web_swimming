from django.db import models

# Create your models here.

# 게시글(post)엔 제목(postname), 내용(contents)이 포함됩니다.
class Post(models.Model):
    postname = models.CharField(max_length = 50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    
    # postname이 post object 대신 나오기
    def __str__(self):
        return self.postname