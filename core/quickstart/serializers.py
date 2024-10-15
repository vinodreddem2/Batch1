from rest_framework import serializers
from quickstart.models import Person,Color

class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Color
        fields = ['color_name']
        


class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        
        # Model you want to serialize
        model = Person
        # model fields
        fields = '__all__'
        # depth=1
        
        def validate(self,data):
            print(data)
            if data['age']<25:
                raise serializers.ValidationError('Age should be greater than 25')
            
            return data
        