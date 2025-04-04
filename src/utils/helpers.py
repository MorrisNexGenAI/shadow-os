# Utility functions
from datetime import datetime

def get_timestamp():
    """Return a formatted timestamp."""
    return datetime.now().isoformat()