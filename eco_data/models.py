from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username= models.CharField(max_length=225, null=True, blank=True)
    # image = models.ImageField(default='default.png', upload_to='profile_pics')
    residence = models.CharField(max_length=255, null=True)
    bio = models.TextField()
    dob = models.DateTimeField()
    



    def __str__(self):
        return f'{self.user.username} Profile'
    

class Company(models.Model):
    companyname=models.CharField(max_length=250)
    bio=models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.companyname
    



class Products(models.Model):
    name=models.CharField(max_length=250)
    # image = models.ImageField(default='default.png', upload_to='profile_pics')
    mens = 'mens'
    ladies = 'ladies'
    children = 'children'
    other = 'other'
    category_choices = [(mens, 'mens'), (ladies, 'ladies'),(children, 'children'),(other, 'other')]
    category =models.CharField(max_length=10, choices=category_choices, default=other)
    description = models.TextField(max_length=5000)
    price=models.DecimalField(max_digits=100000, decimal_places=2)


    def __str__(self):
        return self.name