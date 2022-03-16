from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 
        # fields = ('profile_picture','prof_user','contact_info','bio','all_projects','profile_Id')



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 
        # fields = ('title','details','link','user','image','design','usability','content')


