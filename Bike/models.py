from django.db import models

# Create your models here.
class Bicycle(models.Model):
    owner_name = models.CharField(max_length=100)
    bicycle_name = models.CharField(max_length=100)
    time_taken = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bicycles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bicycle_name
class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50,default='')
    price = models.CharField(max_length=50,default=0)

    def __str__(self):
        return self.title

class CheckIn(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Owner(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)