# LexiLingo

Welcome to MY PROJECT Lexilingo! This project provides several Natural Language Processing (NLP) features, including translation and language detection, POS tagging and NER recognition, text summarization, and sentiment analysis.

## Features

1. **Translation & Language Detection**: Translate text between different languages and detect the language of the given text.
2. **POS Tagging & NER Recognition**: Perform Part-of-Speech (POS) tagging and Named Entity Recognition (NER) on the given text.
3. **Text Summarization**: Generate a concise summary of the provided text.
4. **Sentiment Analysis**: Analyze the sentiment of the given text to determine if it is positive, negative, or neutral.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/nlp-project.git
    cd nlp-project
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Download NLTK data (if not already downloaded):
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('vader_lexicon')
    ```

## Usage

1. Start the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Use the navigation links on the homepage to access the different NLP features.

## Project Structure

nlp-project/
│
├── templates/
│ ├── index.html
│ ├── translation.html
│ ├── pos_ner.html
│ ├── summarization.html
│ └── sentiment_analysis.html
│
├── static/
│ └── css/
│ └── styles.css
│
├── main.py
├── translation.py
├── pos_ner.py
├── summarization.py
└── sentiment_analysis.py


- `templates/`: Contains HTML templates for the web pages.
- `static/css/`: Contains CSS files for styling.
- `main.py`: The main Flask application file.
- `translation.py`: Contains code for translation and language detection.
- `pos_ner.py`: Contains code for POS tagging and NER recognition.
- `summarization.py`: Contains code for text summarization.
- `sentiment_analysis.py`: Contains code for sentiment analysis.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the existing code style and include appropriate tests.

## Acknowledgments

- [NLTK](https://www.nltk.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [spaCy](https://spacy.io/)
