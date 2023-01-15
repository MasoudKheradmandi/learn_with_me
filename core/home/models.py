from django.db import models

# Create your models here.
class Footer(models.Model):
    locations = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    telegram1= models.CharField(max_length=150,verbose_name='Masoud Telegram',null=True)
    telegram2 =  models.CharField(max_length=150,verbose_name='Erfan Telegram',null=True)
    email = models.EmailField(max_length=254)

