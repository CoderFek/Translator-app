from django.forms import ModelForm
from .models import Translation

class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields = ['source_text', 'source_lang', 'target_lang']