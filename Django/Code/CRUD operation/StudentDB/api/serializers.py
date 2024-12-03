from rest_framework import serializers
from .models import Student

#instead of writing manual serializing code we can use ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city'] # if we need id also then fields = ['id', name', 'roll', 'city']

"""
    # ****************** Validation code is written according to their priority level && validation will be same for both ModelSerialize and Serializer **************************
    #Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Must start with R or r')
    name = serializers.CharField(validators=[start_with_r])    
    
    #Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Invalid Roll Number!')
        return value
    #Object Level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='rohit' and ct.lower()!='dhaka':
            raise serializers.ValidationError('City Must be Dhaka')
        return data
"""



"""
           #*************************************** For manually writing serializer *********************************************

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
"""