from django.contrib import admin
from .models import Post,Hakkinda,Comment,Tag

admin.site.register(Post)
admin.site.register(Hakkinda)
admin.site.register(Comment)
admin.site.register(Tag)