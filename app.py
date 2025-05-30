from flask import Flask, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyse/<text>', methods=['GET'])
def analyse_sentiment(text):
    # Analyse sentiment using TextBlob
    analysis = TextBlob(text)
    
    # Determine sentiment polarity
    if analysis.sentiment.polarity > 0:
        sentiment = 'positive'
    elif analysis.sentiment.polarity == 0:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    
    # Prepare response
    response = {
        'text': text,
        'sentiment': sentiment,
        'polarity': analysis.sentiment.polarity,
        'subjectivity': analysis.sentiment.subjectivity
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)