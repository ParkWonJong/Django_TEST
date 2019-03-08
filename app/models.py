#######################################################################################
# model 필드는 페이지의 각 테이블에 들어갈 데이터 형식을 정의한다.
# model을 정의했다면 makemigrations, migrate를 통해 DB와 연동을 하여 테이블을 생성할 것
#######################################################################################
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username



# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.img', blank=True)
    music = models.FileField(blank = True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] +'...'



