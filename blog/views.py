from django.shortcuts import render
from django.urls import reverse

from blog.models import Post,Hakkinda,Comment
from blog.forms import YorumForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User


def yazi_listesi(request):
    # filter(yayinlanma_tarihi__lte=timezone.now())
    post = Post.objects.all().order_by('yayinlanma_tarihi')
    return render(request, "blog/post_list.html", {'posts':post})

def yazi_detayi(request, **kwargs):
    post = Post.objects.get(id=kwargs['post_id'])
    comments = Comment.objects.filter(post_id=post.pk)
    yorumform = YorumForm()
    return render(request, "blog/post_detay.html", {'post': post, 'comments': comments, 'yorum_form':yorumform})

def hakkinda(request):
    hakkinda = Hakkinda.objects.first()
    return render(request, "blog/hakkinda.html", {'hakkinda': hakkinda})

def yorum(request,**kwargs):
    if request.method == "POST":
        form = YorumForm(request.POST)
        post = Post.objects.get(pk=kwargs['post_id'])
        form.instance.post = post
        if form.is_valid():
            form.save()
    return redirect(reverse('yazi_detayi',kwargs={'post_id':post.id}))

def tag(request, **kwargs):
    posts = Post.objects.filter(tags__id=kwargs['tag_id'])
    return render(request, "blog/post_list.html", {'posts':posts})