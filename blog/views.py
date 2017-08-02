from django.shortcuts import render
from blog.models import Post,Hakkinda,Comment
from django.utils import timezone

def yazi_listesi(request):
	# filter(yayinlanma_tarihi__lte=timezone.now())
	post = Post.objects.all().order_by('yayinlanma_tarihi')
	return render(request, "blog/post_list.html", {'posts':post})

def yazi_detayi(request, **kwargs):
	post = Post.objects.get(id=kwargs['post_id'])
	comments = Comment.objects.filter(post_id=post.pk)
	return render(request, "blog/post_detay.html", {'post': post, 'comments': comments})

def hakkinda(request):
	hakkinda = Hakkinda.objects.first()
	return render(request, "blog/hakkinda.html", {'hakkinda': hakkinda})