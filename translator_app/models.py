from django.db import models


# Create your models here.
class Translation(models.Model):
    source_text = models.TextField()
    source_lang = models.CharField(max_length = 30)
    target_lang = models.CharField(max_length = 30)
    target_text = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.source_lang} to {self.target_lang}"