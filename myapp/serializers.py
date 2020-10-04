from rest_framework import serializers
from myapp.models import Resource

class ResSerializer(serializers.ModelSerializer):

    unique_identifier = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    time = serializers.CharField(max_length=50)
    class Meta:
        model = Resource
        fields = '__all__'
