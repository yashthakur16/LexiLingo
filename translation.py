# translation.py
from flask import Blueprint, render_template, request
from googletrans import Translator
from langdetect import detect

translation = Blueprint('translation', __name__)

@translation.route('/translation', methods=['GET', 'POST'])
def translate_text():
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang).text
        detected_lang = detect(text)
        return render_template('translation.html', translated_text=translated_text, detected_lang=detected_lang)
    return render_template('translation.html')
