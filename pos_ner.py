# pos_ner.py
from flask import Blueprint, render_template, request
import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize

pos_ner = Blueprint('pos_ner', __name__)

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

@pos_ner.route('/pos_ner', methods=['GET', 'POST'])
def perform_pos_ner():
    if request.method == 'POST':
        text = request.form['text']
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        ner_entities = ne_chunk(pos_tags)
        return render_template('pos_ner.html', pos_tags=pos_tags, ner_entities=ner_entities)
    return render_template('pos_ner.html')
