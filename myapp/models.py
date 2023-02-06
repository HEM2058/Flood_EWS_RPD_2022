from django.db import models

# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    otp = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    river = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.fname