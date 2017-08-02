from django.db import models
from django.utils import timezone


class Post(models.Model):
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

class Hakkinda(models.Model):
    icerik = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post)
    user = models.ForeignKey('auth.User')