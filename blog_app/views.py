from django.shortcuts import render
from .models import blogpost, postcomment

# Create your views here.

def blog_page(request):
    all_post=blogpost.objects.all
    context={
        'all_post': all_post
    }
    return render(request,'blog_page.html',context)


def search(request):
    q=request.GET.get("q","")   
    all_post=blogpost.objects.filter(title__icontains=q)
    context={
        'all_post': all_post
    }
    return render(request,'blog_page.html',context)


def single_post(request,id):
    comment_body=comment_author= None
    if request.method=='POST':
        comment_body=request.POST.get('comment_body')
        comment_author=request.POST.get('comment_author')
    
    data=blogpost.objects.get(id=id)

    if comment_body and comment_author:
        comment=postcomment(post=data,comment_body=comment_body,comment_author=comment_author)
        comment.save()

    all_comments=postcomment.objects.filter(post=data)

    context={
        'post':data,
        'all_comments':all_comments
    }
    return render(request,'single_post.html',context)


def blogs(request):
    return render(request,'structure.html')

def homepage(request):
    return render(request,'home_page.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')