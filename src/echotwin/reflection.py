# EchoTwin reflection logic
from src.vaultmind.storage import get_similar_thoughts

def get_insight(text, analysis):
    """Generate a reflective insight."""
    sentiment = analysis["sentiment"]
    similar_thoughts = get_similar_thoughts(text)
    
    if sentiment < 0:
        return "You seem down. Is something weighing on you today?"
    elif similar_thoughts:
        last_similar = similar_thoughts[-1][1]  # Text of most recent similar thought
        return f"This reminds me of something you said before: '{last_similar}'. What’s shifted?"
    else:
        return "A fresh thought—want to dig deeper into it?"