from rest_framework import serializers
from django.utils.timezone import now

from streamflix.validators import *
from streamflix.models import Video, Categoria


class VideoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category']
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'title', 'color']
        
class VideoPorCategoriaSerializer(serializers.ModelSerializer):
    
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = ['title','url', 'category']
    
    def get_category(self, obj):
        return now()
 