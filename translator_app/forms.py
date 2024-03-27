from django import forms
from .utils import LANGUAGE_SLUGS

class TranslationForm(forms.Form):
    source_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'style': 'overflow-y: auto;', 'placeholder' : 'Enter source text'}))
    source_lang = forms.ChoiceField(label = 'Source language', choices=LANGUAGE_SLUGS.items)
    target_lang = forms.ChoiceField(label = 'Target language', choices=LANGUAGE_SLUGS.items)
