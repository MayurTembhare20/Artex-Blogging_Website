from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from blog_app import views

urlpatterns = [
     path('',views.homepage,name='homepage'),
     path('blog_page/',views.blog_page,name='blog_page'),
     path('blogs/',views.blogs,name='blogs'),
     path('search/',views.search,name='search'),
     path('post/<id>',views.single_post,name='single_post'),
     path('contact/',views.contact,name='contact'),
     path('about/',views.about,name='about')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
