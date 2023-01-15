from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    contact_list = Course.objects.all()
    paginator = Paginator(contact_list, 1)
    page_number = request.GET.get('page')
    course = paginator.get_page(page_number)
    context = {
        'course':course
    }
    return render(request,'index.html',context)