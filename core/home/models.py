from django.db import models

# Create your models here.
class Footer(models.Model):
    locations = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    telegram1= models.CharField(max_length=150,verbose_name='Masoud Telegram',null=True)
    telegram2 =  models.CharField(max_length=150,verbose_name='Erfan Telegram',null=True)
    email = models.EmailField(max_length=254)

class NavOne(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار',blank=True,null=True)    
    def __str__(self):
        return self.name

class NavTwo(models.Model):
    parent = models.ForeignKey(NavOne,on_delete=models.PROTECT)
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار')    
    def __str__(self):
        return self.name


class HeaderDetail(models.Model):
    logo = models.ImageField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    
