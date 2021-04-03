from django.db import models

# Create your models here.

class Questions(models.Model):
    questions = models.CharField(max_length=250)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correctAnswer= models.CharField(max_length=30,default="hello")
    fiftyFiftyId1 = models.CharField(max_length=1,default="h")
    fiftyFiftyId2 = models.CharField(max_length=1,default="h")

class users(models.Model):
    fullname = models.CharField(max_length=50)
    givenname = models.CharField(max_length=50)
    familyName = models.CharField(max_length=20)
    image_url= models.CharField(max_length=300)
    email = models.CharField(max_length=200)