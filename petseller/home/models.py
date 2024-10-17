from django.db import models
from django.contrib.auth.models import User

from .choices import ANIMAL_CHOICES,ANIMAL_GENDER


class Category(models.Model):
    Category_name = models.CharField(max_length=100)


class AnimalBreed(models.Model):
    animal_breed =models.CharField(max_length=100) 

class AnimalColor(models.Model):
    animal_color = models.CharField(max_length=100)
    
class Animal(models.Model):
    # related_name--->reverse mapping (u can access all animals from user--->User.)
    animal_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='animal')
    # If the choices are going to be static then we can use this  --> animal_category = models.CharField(max_length=100,choices=ANIMAL_CHOICES)
    animal_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='animal_category')
    animal_views = models.IntegerField(default=0)
    animal_likes = models.IntegerField(default=0)
    animal_description = models.TextField()
    animal_slug = models.SlugField(max_length=1000,unique=True)
    animal_gender = models.CharField(max_length=100,choices=ANIMAL_GENDER)
    animal_breed = models.ManyToManyField(AnimalBreed,null=True)
    animal_color = models.ManyToManyField(AnimalColor)
    
class AnimalLocation(models.Model):
    animal= models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='animal_location')
    location=models.CharField(max_length=100)


class AnimalImage(models.Model):
    animal= models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='animal_Image')
    image = models.ImageField(upload_to='animals')