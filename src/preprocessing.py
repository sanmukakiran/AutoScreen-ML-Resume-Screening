import re
import sys
if sys.version_info >= (3, 11) and not hasattr(re, 'template'):
    re.template = re.compile # Monkeypatch for Python 3.14 compat
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_nltk_data():
    """Downloads required NLTK datasets politely."""
    resources = {
        'tokenizers/punkt': 'punkt',
        'tokenizers/punkt_tab': 'punkt_tab',
        'corpora/stopwords': 'stopwords',
        'corpora/wordnet': 'wordnet'
    }
    
    for path, res in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            logger.info(f"Downloading NLTK resource: {res}")
            nltk.download(res, quiet=True)

# Ensure resources are available
download_nltk_data()

def clean_text(text):
    """
    Cleans the input text by converting to lowercase, removing special characters,
    and extra whitespaces, while preserving common programming language symbols.
    """
    if not isinstance(text, str):
        return ""
    
    # Convert to lower case
    text = text.lower()
    
    # Remove special characters except alphanumeric, spaces, +, and #
    # This preserves 'c++', 'c#', etc.
    text = re.sub(r'[^a-z0-9\s+#]', ' ', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_text(text):
    """
    Cleans text, tokenizes, removes stop words, and lemmatizes to prepare for ML.
    """
    text = clean_text(text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    
    return " ".join(lemmatized)

if __name__ == "__main__":
    sample = "I am a Data Scientist! I have 4+ years of experience in Python, C++, and Pandas."
    print("Original:", sample)
    print("Preprocessed:", preprocess_text(sample))
