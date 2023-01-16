from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Course,Comment
from django.core.paginator import Paginator
from home.models import Footer
from .forms import CommentForm
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
    comments =Comment.objects.filter(is_show=True,course_id=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request,'پیام شما با موفقیت ثبت شد . با تایید ادمین نمایش داده میشود')
        else:
            messages.error(request,'متاسفانه مشکلی پیش امده است , لطفا دوباره امتحان کنید.')
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
    context ={
        'details':x,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'course_detail.html',context)

def footer(request):
    context = {
        'footer':Footer.objects.all().last()
    }
    return render(request,'footer.html',context)



def Search(request):
    search = request.GET.get('filter_name')
    course=Course.objects.filter(name__icontains=search)
    

    context = {
        'course':course,
    }
    return render(request,'search_listview.html',context)