import sqlite3
from config.settings import DB_PATH
from src.utils.helpers import get_timestamp

def init_db():
    """Initialize the database with a thoughts table."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS thoughts
                 (timestamp TEXT, text TEXT, sentiment REAL, keywords TEXT)''')
    conn.commit()
    conn.close()

def store_thought(text, sentiment, keywords):
    """Store a thought with metadata."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO thoughts VALUES (?, ?, ?, ?)",
              (get_timestamp(), text, sentiment, keywords))
    conn.commit()
    conn.close()

def get_all_thoughts():
    """Retrieve all thoughts."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM thoughts")
    thoughts = c.fetchall()
    conn.close()
    return thoughts

def get_similar_thoughts(text):
    """Find thoughts with similar text."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM thoughts WHERE text LIKE ?", ('%'+text+'%',))
    similar = c.fetchall()
    conn.close()
    return similar