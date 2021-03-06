from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.yazi_listesi, name='yazi_listesi'),
    url(r'^detay/(?P<post_id>[\d]+)/$', views.yazi_detayi, name='yazi_detayi'),
    url(r'hakkinda/$', views.hakkinda, name='hakkinda'),
    url(r'^yorum/(?P<post_id>[\d]+)/$', views.yorum, name='yorum'),
    url(r'^tag/(?P<tag_id>[\d]+)/$', views.tag, name='tags'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)