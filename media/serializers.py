from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def validate(self, data):
        introduction = data.get('introduction')
        notice = data.get('notice')

        if introduction and notice:
            raise serializers.ValidationError(
                "You can choose either an introduction or a notice, not both.")

        return data
