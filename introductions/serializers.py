from rest_framework import serializers
from .models import introduction

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = introduction
        fields = '__all__'