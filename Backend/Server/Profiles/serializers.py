from rest_framework import serializers

from .models import CustomersProfile, EmployeeProfile, EmployeeSkils

from Users.serializers import UserSerializer



class CustomersProfileSerializer(serializers.ModelSerializer):
    
    customer = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomersProfile
        fields = '__all__'
    
    def get_customer(self, obj):
        return obj.customer.username



class EmployeeProfileSerializer(serializers.ModelSerializer):
    
    employee = serializers.SerializerMethodField()
    
    class Meta:
        model = EmployeeProfile
        fields = '__all__'

    def get_employee(self, obj1):
        return obj1.employee.username

 
class EmployeeSkilsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeSkils
        fields = '__all__'
