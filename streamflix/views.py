from config.settings import ALLOWED_HOSTS
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from streamflix.models import Video, Categoria
from streamflix.serializers import VideoPorCategoriaSerializer, VideoSerializer, CategoriaSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'videos': reverse('video-list', request=request, format=format),
        'categorias': reverse('categoria-list', request=request, format=format)
    })


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
       
class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
  
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        content = {'Message': 'Video excluído com sucesso.'}
        return Response(
            data=content,
            status=status.HTTP_204_NO_CONTENT
        )
    
    
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['color']
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        content = {'Message': 'Categoria excluída com sucesso.'}
        return Response(
            data=content,
            status=status.HTTP_204_NO_CONTENT
        )


class VideoPorCategoria(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Video.objects.filter(category_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = VideoPorCategoriaSerializer


class VideoFree(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Video.objects.filter(category_id=1)
        return queryset
    
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]