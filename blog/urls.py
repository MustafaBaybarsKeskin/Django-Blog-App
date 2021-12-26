from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.blogIndex, name = 'blogIndex'),
    path('blog/<int:id>',views.blogDetail, name = "blogDetail"), 
    path('about', views.about, name='about_us'),
    path('blog/yazılım', views.ycategory, name = 'ycategory'),
    path('blog/genel', views.gcategory, name = 'gcategory'),
    path('blog/eglence', views.egcategory, name = 'egcategory'),
    path('blog/elektronik', views.elcategory, name = 'elcategory'),
    path('blog/search', views.search, name = 'search'),

    url(r'^img/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 