from textblob import TextBlob

def analyze_thought(text):
    """Analyze text for sentiment and keywords."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    keywords = ','.join(blob.noun_phrases) if blob.noun_phrases else ""
    return {"sentiment": sentiment, "keywords": keywords}