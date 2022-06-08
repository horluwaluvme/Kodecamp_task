from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phonenumber = models.IntegerField
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add = True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length = 50)
    sex = models.CharField(max_length = 50)
    phonenumber = models.IntegerField
    post = models.CharField(max_length = 50)
    patients = models.ForeignKey("People", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    productId = models.CharField(max_length = 50)
    manufacD = models.DateField(max_length=15)
    expD = models.DateField(max_length=15)
    description = models.CharField(max_length = 50)

    def __str__(self):
        return self.productId

class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    postalcode = models.SmallIntegerField
    country = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.city


class Bio(models.Model):
    username = models.OneToOneField(People, on_delete=models.CASCADE)
    educationBg = models.CharField(max_length = 50) 
    hobbies = models.CharField(max_length = 50)

    def __str__(self):
        return self.hobbies

#python manage.py makemigration
#python manage.py migrate