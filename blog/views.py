from django.shortcuts import render
from .models import Blog,BlogImage,BlogParagraph

def BlogView(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request,"blog_list.html",context)


def DetailBlogView(request,id):
    context = {}
    blog_data = Blog.objects.get(pk=id) 
    context['blog'] = blog_data
    blog_paragraphs = BlogParagraph.objects.filter(blog=blog_data)
    blog_images =  BlogImage.objects.filter(blog=blog_data)
    context['combined_data'] = list(zip(blog_paragraphs, blog_images))
    return render(request,"detail_blog.html",context)