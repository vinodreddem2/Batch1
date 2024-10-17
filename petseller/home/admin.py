from django.contrib import admin
from .models import Animal,Category,AnimalBreed,AnimalColor,AnimalImage,AnimalLocation
# Register your models here.

admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(AnimalBreed)
admin.site.register(AnimalColor)
admin.site.register(AnimalImage)
admin.site.register(AnimalLocation)