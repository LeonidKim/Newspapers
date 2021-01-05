from django.db import models


# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)


class NewsPaper(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    number = models.IntegerField()
    edition = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(null=True)


class Subscription(models.Model):
    client_id = models.CharField(max_length=50)
    newspaper_id = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    duration = models.IntegerField()
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
