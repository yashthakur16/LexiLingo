# main.py
from flask import Flask, render_template
from translation import translation
from pos_ner import pos_ner
from summarization import summarization
from sentiment_analysis import sentiment_analysis  # Import the sentiment analysis Blueprint

app = Flask(__name__)

app.register_blueprint(translation)
app.register_blueprint(pos_ner)
app.register_blueprint(summarization)
app.register_blueprint(sentiment_analysis)  # Register the sentiment analysis Blueprint

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
