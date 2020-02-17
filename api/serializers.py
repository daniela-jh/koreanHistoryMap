from rest_framework import serializers
from .models import Content
from django.contrib.auth.models import User

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'locationName',
            'locationText1',
            'locationText2',
            'locationText3',
            'locationText4',
            'locLat',
            'locLng',
        )