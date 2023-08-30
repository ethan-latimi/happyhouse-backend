from rest_framework import serializers
from .models import photo, notice, comment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = notice
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
