from django.contrib import admin

# Register your models here.
from .models import Footer,NavOne,NavTwo,HeaderDetail


admin.site.register(Footer)
admin.site.register(NavOne)
admin.site.register(NavTwo)
admin.site.register(HeaderDetail)