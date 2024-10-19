from rest_framework import serializers

from .models import AnimalBreed,AnimalColor,AnimalImage,Animal,AnimalLocation,Category


class CategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = Category
        fields = ['category_name']

class AnimalBreedSerializer(serializers.ModelSerializer):
     class Meta:
        model = AnimalBreed
        fields ='__all__' 

class AnimalColorSerializer(serializers.ModelSerializer):
     class Meta:
        model = AnimalColor
        fields ='__all__' 
        
class AnimalSerializer(serializers.ModelSerializer):
   
     animal_category=serializers.SerializerMethodField()  #CategorySerializer()--> This is for full description
     animal_color_serializer = AnimalColorSerializer(many=True)
     
      # This method is to flatten the object     
     def get_animal_category(self,obj):
        return obj.animal_category.category_name
     
   #   def get_animal_color(self,obj):
   #      return obj.animal_color.animal_color      
      
      #  This method is to alter the way the data is sent in the response 
     def to_representation(self, instance):
         # animal_color_serializer = AnimalColorSerializer(instance.animal_color.all(),many=True)
         
         payload = {
            "animal_category":instance.animal_category.category_name,
            "animal_name":instance.animal_name,
            "animal_views":instance.animal_views,
            "animal_likes":instance.animal_likes,
            "animal_description":instance.animal_description,
            # "animal_color":animal_color_serializer.data,
            "animal_color":instance.animal_color_serializer.animal_color
         }
         return payload
     
     class Meta:
        model = Animal
        exclude=['updated_at']

class AnimalLocationSerializer(serializers.ModelSerializer):
     class Meta:
        model = AnimalLocation
        fields ='__all__' 

class AnimalImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = AnimalImage
        fields ='__all__'  