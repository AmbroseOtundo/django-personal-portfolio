from django.shortcuts import render, get_object_or_404# this 404 refs the detail function
from .models import Projectblog
# Create your views here.
def all_blogs(request):
    # order by date then last 5 blogs
    blogs = Projectblog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    # grab one object.
    blog  = get_object_or_404(Projectblog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})