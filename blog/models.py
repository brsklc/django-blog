from django.db import models
from django.utils import timezone


class Post(models.Model):
    tags = models.ManyToManyField('blog.Tag',related_name='posts')
    arka_plan_resmi = models.ImageField(upload_to='resim/', null=True, blank=True)
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=50)
    kisa_baslik = models.CharField(max_length=100,null=True, blank=True)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(
           default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
           blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Hakkinda(models.Model):
    icerik = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post)
    create_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)

