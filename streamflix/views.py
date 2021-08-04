# # CRUD com APIView

# from rest_framework import status, serializers, generics, filters
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse

# from django_filters.rest_framework import DjangoFilterBackend

# from streamflix.models import Video, Categoria
# from streamflix.serializers import VideoSerializer, CategoriaSerializer


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'videos': reverse('video-list', request=request, format=format),
#         'categorias': reverse('categoria-list', request=request, format=format)
#     })


# class VideoList(APIView):
#     """Lista ou Cria um novo vídeo"""
    
#     # format=None, diz que nossa resposta pode ser qualquer tipo de arquivo
#     def get(self, request, format=None):
#         videos = Video.objects.all()
#         # many=True diz que conseguimos serializar querysets, em vez de só instancias de modelos.
#         serializer = VideoSerializer(videos, many=True)        
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         # No post não coloca o atributo many como True. Many como True só quando for queryset
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED,)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VideoDetail(APIView):
#     """Retrieve(Read), Update ou Delete um vídeo"""
    
#     def get_object(self, pk):
#         try:
#             return Video.objects.get(pk=pk)
#         except Video.DoesNotExist:
#             raise NotFound(
#                 {'Error': 'Vídeo não encontrado.'}
#             )
    
#     def get(self, request, pk, format=None):
#         video = self.get_object(pk)
#         serializer = VideoSerializer(video)
#         return Response(serializer.data)       
    
#     def put(self, request, pk, format=None):
#         video = self.get_object(pk)
#         serializer = VideoSerializer(video, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         video = self.get_object(pk)
#         video.delete()
#         content = {'Message': 'Vídeo deletado com sucesso'}
#         return Response(
#             data=content,
#             status=status.HTTP_204_NO_CONTENT
#         )

    
# class CategoriaList(APIView):
    
#     def get(self, request, format=None):
#         queryset = Categoria.objects.all()
#         serializer = CategoriaSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         data = request.data
#         desserializer = CategoriaSerializer(data=data)
#         if desserializer.is_valid():
#             desserializer.save()
#             return Response(desserializer.data, status=status.HTTP_201_CREATED)
#         return Response(desserializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
# class CategoriaDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Categoria.objects.get(pk=pk)
#         except Categoria.DoesNotExist:
#             raise NotFound({
#                 'Error': 'Categoria não encontrada.'
#             })
    
#     # GET
#     def get(self, request, pk, format=None):
#         categoria = self.get_object(pk)
#         serializer = CategoriaSerializer(categoria)
#         return Response(serializer.data)
    
#     # PUT / PATCH
#     def put(self, request, pk, format=None):
#         categoria = self.get_object(pk)
#         deserializer = CategoriaSerializer(categoria, data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(data=deserializer.data)
#         else:
#             return Response(serializers.erros, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE
#     def delete(self, request, pk, format=None):
#         categoria = self.get_object(pk)
#         categoria.delete()
#         content = {'Message': 'Categoria deletada com sucesso.'}
#         return Response(
#             data=content,
#             status=status.HTTP_204_NO_CONTENT
#         )

# ================= CRUD com generics

from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django_filters.rest_framework import DjangoFilterBackend

from streamflix.models import Video, Categoria
from streamflix.serializers import VideoPorCategoriaSerializer, VideoSerializer, CategoriaSerializer



@api_view(['GET'])
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