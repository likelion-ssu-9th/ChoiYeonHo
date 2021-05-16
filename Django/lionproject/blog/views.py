from django.shortcuts import render, get_object_or_404
from .models import Blog 

def home(request):
    blogs = Blog.objects.all() #Blog에 있는 객체 모두 가져와서 blogs에 저장
    return render(request, 'home.html', {'blogs': blogs}) #blogs변수가 'blogs'에 담겨서 html로 이동

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog': blog})