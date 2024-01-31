from django.shortcuts import render
from googletrans import Translator
from .forms import TranslationForm
from .models import Translation
# Create your views here.

def translate_view(request):
    translated_text = ''

    if request.method == 'POST':
        form = TranslationForm(request.POST)

        if form.is_valid():
            source_text = form.cleaned_data['source_text']
            source_lang_slug = form.cleaned_data['source_lang']
            target_lang_slug = form.cleaned_data['target_lang']


            try:
                #Google API integration
                translator = Translator()
                translation = translator.translate(
                    source_text,
                    src = source_lang_slug,
                    dest = target_lang_slug
                )
                translated_text = translation.text


                # Translation.objects.create(
                #     source_text = source_text,
                #     source_lang_slug = source_lang_slug,
                #     target_lang_slug = target_lang_slug,
                #     translated_text = translated_text
                # )

                new_translation = Translation(
                source_text=source_text,
                source_lang_slug=source_lang_slug,
                target_lang_slug=target_lang_slug,
                translated_text=translated_text
                )
                new_translation.save()
                # Translation.target_text = translated_text
                # Translation.save()
            except Exception as e:
                print(f"Error during translation: {e}")
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form, 'translated_text': translated_text})