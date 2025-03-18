import re
import logging
from collections import Counter

def analyze_logs(log_content):
    """
    Analyzes log content by counting word frequency.

    :param log_content: String containing log data
    :return: List of tuples with words and their counts, sorted by frequency
    """
    try:
        words = re.findall(r'\b\w+\b', log_content)
        word_counts = Counter(words)
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_counts
    except Exception as e:
        logging.error(f"Error analyzing logs: {e}")
        return []
