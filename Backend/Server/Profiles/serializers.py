from rest_framework import serializers

from .models import SimpleUserProfile, EmployeeProfile, EmployeeSkils

from Users.serializers import UserSerializer



class SimpleUserProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = SimpleUserProfile
        fields = ['id', 'full_name', 'profile_picture', 'bio', 'user']
        
    def get_user(self, obj):
        return obj.user.username
    
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()  # Save the updated instance
        return instance


class EmployeeSkilsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeSkils
        fields = ['skill', 'mastery']


class EmployeeProfileSerializer(serializers.ModelSerializer):
    
    skils = serializers.SerializerMethodField()
    
    employee = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeProfile
        fields = ['id', 'full_name', 'employee_stack', 'job_title', 'bio', 'profile_picture', 'skils', 'years_of_experience', 'employee']
    
    
    def get_employee(self, obj):
        return obj.employee.username
    
    def get_skils(self, obj):
        skils = obj.skils.all()
        serializer = EmployeeSkilsSerializer(skils, many=True)
        return serializer.data

    def update(self, instance, validated_data):
        
        # Update the instance fields with the validated data
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.employee_stack = validated_data.get('employee_stack', instance.employee_stack)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.years_of_experience = validated_data.get('years_of_experience', instance.years_of_experience)

        # Handle the many-to-many field for skills
        skills_data = validated_data.get('skils', None)
        
        if skills_data is not None:
            instance.skils.set(skills_data)  # Update the many-to-many relationship
            
        instance.save()  # Save the updated instance
        return instance