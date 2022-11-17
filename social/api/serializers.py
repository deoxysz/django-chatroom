from rest_framework.serializers import ModelSerializer

from social.models import Room


class ChatSerializer(ModelSerializer):
    
    class Meta:
        model = Room
        fields = '__all__'