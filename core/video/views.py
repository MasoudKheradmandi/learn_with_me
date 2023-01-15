from django.shortcuts import render,get_object_or_404
from .models import Course
from django.core.paginator import Paginator
from home.models import Footer
# Create your views here.
def home(request):
    contact_list = Course.objects.all()
    paginator = Paginator(contact_list, 1)
    page_number = request.GET.get('page')
    course = paginator.get_page(page_number)
    context = {
        'course':course,
    }
    return render(request,'index.html',context)


def detailview(request,id):
    x = get_object_or_404(Course,id=id)
    context ={
        'details':x
    }
    return render(request,'course_detail.html',context)

def footer(request):
    context = {
        'footer':Footer.objects.get()
    }
    pass
