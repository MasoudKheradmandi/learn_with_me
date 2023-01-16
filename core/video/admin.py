from django.contrib import admin
from .models import Course,Video,Category,Comment
# Register your models here.


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Comment)
