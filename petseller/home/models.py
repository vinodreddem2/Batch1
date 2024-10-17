from django.db import models
from django.contrib.auth.models import User
from .choices import ANIMAL_GENDER

import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at= models.DateField( auto_now_add=True)
    updated_at= models.DateField( auto_now_add=True)
    
    class Meta:
        abstract=True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class AnimalBreed(BaseModel):
    breed =models.CharField(max_length=100) 
    
    def __str__(self):
        return self.breed

class AnimalColor(BaseModel):
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color
    
class Animal(BaseModel):
    # related_name--->reverse mapping (u can access all animals from user--->User.)
    animal_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='animals')
    # If the choices are going to be static then we can use this  --> animal_category = models.CharField(max_length=100,choices=ANIMAL_CHOICES)
    animal_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    animal_name = models.CharField(max_length=100)
    animal_views = models.IntegerField(default=0)
    animal_likes = models.IntegerField(default=0)
    animal_description = models.TextField()
    animal_slug = models.SlugField(max_length=224,unique=True)
    animal_gender = models.CharField(max_length=100,choices=ANIMAL_GENDER)
    animal_breed = models.ManyToManyField(AnimalBreed)
    animal_color = models.ManyToManyField(AnimalColor)
    
    def __str__(self):
        return self.animal_name    
    
    class Meta:
        ordering=['animal_name']
    
class AnimalLocation(BaseModel):
    animal= models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='location')
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.animal.animal_name} Location'

class AnimalImage(BaseModel):
    animal= models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='animals')
    
    def __str__(self):
        return f'{self.animal.animal_name} Image'