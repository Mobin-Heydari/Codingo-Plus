from rest_framework import serializers

from .models import CustomersProfile, EmployeeProfile, EmployeeSkils





class CustomersProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomersProfile
        fields = '__all__'
        


class EmployeeProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeProfile
        fields = '__all__'


 
class EmployeeSkilsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeSkils
        fields = '__all__'
