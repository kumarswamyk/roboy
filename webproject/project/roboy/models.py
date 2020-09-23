from django.db import models


class user_details(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
   

    
class user_images(models.Model):
        images=models.ImageField(null=True ,blank=True)
        price=models.IntegerField()
        caption=models.CharField(max_length=100)
    
class user_profile(models.Model):
        name=models.CharField(max_length=100)

