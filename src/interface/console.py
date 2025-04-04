from src.vaultmind.storage import init_db, store_thought, get_all_thoughts
from src.vaultmind.analysis import analyze_thought
from src.echotwin.reflection import get_insight

def run_console():
    """Run the Shadow OS console interface."""
    init_db()  # Set up DB on first run
    print("Welcome to Shadow OS: The Thought Chamber")
    
    while True:
        thought = input("\nWhat’s on your mind? (type 'view' for timeline, 'quit' to exit): ")
        if thought.lower() == 'quit':
            print("Goodbye.")
            break
        elif thought.lower() == 'view':
            thoughts = get_all_thoughts()
            if thoughts:
                for t in thoughts:
                    print(f"{t[0]}: {t[1]} (Sentiment: {t[2]})")
            else:
                print("No thoughts recorded yet.")
        else:
            analysis = analyze_thought(thought)
            store_thought(thought, analysis["sentiment"], analysis["keywords"])
            insight = get_insight(thought, analysis)
            print("EchoTwin:", insight)