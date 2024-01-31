from django.db import models


# Create your models here.
class Translation(models.Model):
    source_text = models.TextField()
    source_lang_slug = models.CharField(max_length=5, default='')  
    target_lang_slug = models.CharField(max_length=5, default='')
    translated_text = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.source_lang_slug} to {self.target_lang_slug}"
    
    class Meta:
        ordering = ['-id']      #ordering the ids in descending order i.e. the latest comes first