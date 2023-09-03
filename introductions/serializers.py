from rest_framework import serializers
from .models import Introduction


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'
