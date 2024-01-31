from django import forms
from .models import Translation
from .utils import LANGUAGE_SLUGS

class TranslationForm(forms.Form):
    source_text = forms.CharField(label = 'Source Text', widget=forms.Textarea)
    source_lang = forms.ChoiceField(label = 'Source language', choices=LANGUAGE_SLUGS.items)
    target_lang = forms.ChoiceField(label = 'Target language', choices=LANGUAGE_SLUGS.items)