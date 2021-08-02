from django.contrib import admin
from streamflix.models import Video, Categoria

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    ordering = ['id']

    
admin.site.register(Video, VideoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    ordering = ['id']
    
    class Meta:
        ordering = ['id']
    
admin.site.register(Categoria, CategoriaAdmin)
