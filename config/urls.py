from django.contrib import admin
from django.urls import path, re_path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from streamflix import views

# Rota Principal
#router = routers.DefaultRouter()

# Rotas secundárias
#router.register('videos', VideoViewSet, basename='videos')
#router.register('videos/<int:pk>', VideoIdViewSet, basename='videosid')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root),
    path('videos/', views.VideoList.as_view(), name='video-list'),
    path('videos/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('categorias/<int:pk>/videos/', views.VideoPorCategoria.as_view(), name='video-por-categoria')

]

#urlpatterns = format_suffix_patterns(urlpatterns)