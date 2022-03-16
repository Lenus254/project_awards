from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =fields = '__all__' 
        # fields = ('title','details','link','user','image','design','usability','content')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_picture','prof_user','contact_info','bio','all_projects','profile_Id')


