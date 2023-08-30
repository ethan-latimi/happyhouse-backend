from rest_framework import serializers
from .models import curriculum


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = curriculum
        fields = '__all__'
