# sentiment_analysis.py
from flask import Blueprint, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

sentiment_analysis = Blueprint('sentiment_analysis', __name__)

@sentiment_analysis.route('/sentiment_analysis', methods=['GET', 'POST'])
def analyze_sentiment():
    if request.method == 'POST':
        text = request.form['text']
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        sentiment_label = get_sentiment_label(sentiment_scores)
        return render_template('sentiment_analysis.html', text=text, sentiment_label=sentiment_label)
    return render_template('sentiment_analysis.html')

def get_sentiment_label(sentiment_scores):
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
