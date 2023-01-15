from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
        
class Course(models.Model):
    recorder = (
        ('AmirMasoud Kheradmandi','AmirMasoud Kheradmandi'),
        ('Erfan Karimi','Erfan Karimi'),
    )
    LEVEL = (
        ('پیشرفته','پیشرفته'),
        ('مقدماتی','مقدماتی'),
        ('متوسط','متوسط')
    )
    name = models.CharField(max_length=250)
    image = models.ImageField()
    # time
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    Author = models.CharField(choices=recorder,max_length=100,default='AmirMasoud Kheradmandi')
    level = models.CharField(max_length=100,choices=LEVEL,default='متوسط')
    info = RichTextField(null=True)

    def __str__(self):
        return self.name



class Video(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150,verbose_name='نام ویدئو')

    video = models.FileField()
    time = models.IntegerField(null=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title
