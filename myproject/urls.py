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
]