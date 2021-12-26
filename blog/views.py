from django.db.models.fields import CharField
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import Http404
from .models import Blog
from django.db.models import Count

def blogIndex(request):   
    blogsPost1 = Blog.objects.all().order_by('-created_date')[0:3]
    blogsPost2 = Blog.objects.all().order_by('-created_date')[3:6]
    blogsPost3 = Blog.objects.all().order_by('-created_date')[6:]
    BlogPostMostViews = Blog.objects.filter().order_by('-post_views', '-created_date')[0:3]

    context = {
        'blogsPost1': blogsPost1,
        'blogsPost2': blogsPost2,
        'blogsPost3': blogsPost3,
        'BlogPostMostViews': BlogPostMostViews,
    }
    
    return render(request, 'blog/blog.html', context)

def blogDetail(request,id):    
    blogPostDetail = get_object_or_404(Blog,id = id)
    blogPostDetail.post_views = blogPostDetail.post_views + 1
    blogPostDetail.save()

    
    

    context = {
        'blogPostDetail': blogPostDetail,  
    }

    return render(request,"blog/blogdetail.html", context)

def ycategory(request):
    bpost = Blog.objects.all().order_by('-created_date',)
    bpost2 = Blog.objects.all().order_by('-created_date',).filter(category = "GENEL")
    bpost3 = Blog.objects.all().order_by('-created_date',).filter(category = "ELEKTRONIK")
    bpost4 = Blog.objects.all().order_by('-created_date',).filter(category = "YAZILIM")
    bpost5 = Blog.objects.all().order_by('-created_date',).filter(category = "EGLENCE")
    
    context = {
        'bpost': bpost,
        'bpost2':bpost2,
        'bpost3':bpost3,
        'bpost4':bpost4,
        'bpost5':bpost5,
        
    }

    return render(request, 'blog/category/yazılım.html', context)

def gcategory(request):
    bpost = Blog.objects.all().order_by('-created_date',)
    bpost2 = Blog.objects.all().order_by('-created_date',).filter(category = "GENEL")
    bpost3 = Blog.objects.all().order_by('-created_date',).filter(category = "ELEKTRONIK")
    bpost4 = Blog.objects.all().order_by('-created_date',).filter(category = "YAZILIM")
    bpost5 = Blog.objects.all().order_by('-created_date',).filter(category = "EGLENCE")
    
    context = {
        'bpost': bpost,
        'bpost2':bpost2,
        'bpost3':bpost3,
        'bpost4':bpost4,
        'bpost5':bpost5,
        
    }

    return render(request, 'blog/category/genel.html', context)

def egcategory(request):
    bpost = Blog.objects.all().order_by('-created_date',)
    bpost2 = Blog.objects.all().order_by('-created_date',).filter(category = "GENEL")
    bpost3 = Blog.objects.all().order_by('-created_date',).filter(category = "ELEKTRONIK")
    bpost4 = Blog.objects.all().order_by('-created_date',).filter(category = "YAZILIM")
    bpost5 = Blog.objects.all().order_by('-created_date',).filter(category = "EGLENCE")
    
    context = {
        'bpost': bpost,
        'bpost2':bpost2,
        'bpost3':bpost3,
        'bpost4':bpost4,
        'bpost5':bpost5,
        
    }

    return render(request, 'blog/category/eglence.html', context)

def elcategory(request):
    bpost = Blog.objects.all().order_by('-created_date',)
    bpost2 = Blog.objects.all().order_by('-created_date',).filter(category = "GENEL")
    bpost3 = Blog.objects.all().order_by('-created_date',).filter(category = "ELEKTRONIK")
    bpost4 = Blog.objects.all().order_by('-created_date',).filter(category = "YAZILIM")
    bpost5 = Blog.objects.all().order_by('-created_date',).filter(category = "EGLENCE")
    
    context = {
        'bpost': bpost,
        'bpost2':bpost2,
        'bpost3':bpost3,
        'bpost4':bpost4,
        'bpost5':bpost5,
        
    }
    
    return render(request, 'blog/category/elektronik.html', context)

def search(request):
    keyword = request.GET.get("keyword")
    if keyword:
        searchblog = Blog.objects.filter(title__contains = keyword)
        return render(request,"blog/search.html",{"searchblog":searchblog})
    elif keyword==None:
        return render(request,"blog/search.html")

def error_404(request, exception):
    return render(request, '404.html')

def about(request):
    return render(request, 'partials/_about.html')