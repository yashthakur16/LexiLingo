# summarization.py
from flask import Blueprint, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

summarization = Blueprint('summarization', __name__)

@summarization.route('/summarization', methods=['GET', 'POST'])
def generate_summary():
    if request.method == 'POST':
        text = request.form['text']
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 2)  # 2 represents the number of sentences in the summary
        summary_text = " ".join(str(sentence) for sentence in summary)
        return render_template('summarization.html', summary=summary_text)
    return render_template('summarization.html')
