# main.py
from flask import Flask, render_template
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

from translation import translation
from pos_ner import pos_ner
from summarization import summarization
from sentiment_analysis import sentiment_analysis  # Import the sentiment analysis Blueprint

application = Flask(__name__)

application.register_blueprint(translation)
application.register_blueprint(pos_ner)
application.register_blueprint(summarization)
application.register_blueprint(sentiment_analysis)  # Register the sentiment analysis Blueprint

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)
