from django.shortcuts import render
from googletrans import Translator
from .forms import TranslationForm
# Create your views here.

def translate_view(request):
    translated_text = ''

    if request.method == 'POST':
        form = TranslationForm(request.POST)

        if form.is_valid():
            translation = form.save()

            #Google API integration
            translator = Translator()
            translated_text = translator.translate(
                translation.source_text,
                src = translation.source_lang,
                dest = translation.target_lang
            ).text

            translation.target_text = translated_text
            translation.save()
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form, 'translated_text': translated_text})