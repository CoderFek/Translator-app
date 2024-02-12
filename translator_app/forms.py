from django import forms
from .models import Translation
from .utils import LANGUAGE_SLUGS

class TranslationForm(forms.Form):
    source_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'style': 'overflow-y: auto;', 'placeholder' : 'Enter source text'}))
    source_lang = forms.ChoiceField(label = 'Source language', choices=LANGUAGE_SLUGS.items)
    target_lang = forms.ChoiceField(label = 'Target language', choices=LANGUAGE_SLUGS.items)

# class TranslationForm(forms.ModelForm):
#     class Meta:
#         model = Translation
#         fields = ['source_text', 'source_lang_slug', 'target_lang_slug']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Customize the source_text field with a smaller text area
#         self.fields['source_text'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 40, 'style': 'overflow-y: auto;'})
        
#         # Adjust the style of the source_language and target_language fields
#         self.fields['source_lang_slug'].widget.attrs['style'] = 'display: block; margin-bottom: 10px;'
#         self.fields['target_lang_slug'].widget.attrs['style'] = 'display: block; margin-bottom: 10px;'

#         self.fields['source_lang_slug'].choices = LANGUAGE_SLUGS.items
#         self.fields['target_lang_slug'].choices = LANGUAGE_SLUGS.items