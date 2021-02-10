from rest_framework import serializers
from .models import Meme
 
 
 
class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['id', 'meme_owner','caption' ,'url']


class NewMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['caption' ,'url']