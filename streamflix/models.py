from django.db import models
   
class Categoria(models.Model):
    
    CATEGORY = [
        ('FRE','Free'),
        ('ENT','Entrepreneurship'),
        ('FIN','Finances'),
        ('GAM','Games'),
        ('HEA','healthy'),
        ('MOV','Movies'),
        ('NER','Nerd'),
        ('PRO','Programming'),
        ('TEC','Technology'),
        ('TRI','Trips'),   
    ]
    
    title = models.CharField(max_length=3, choices=CATEGORY, blank=False, null=False, default='FRE')
    color = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    
    title = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=500, blank=False)
    url = models.URLField(max_length=300, blank=False, null=False, unique=True)
    category = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
