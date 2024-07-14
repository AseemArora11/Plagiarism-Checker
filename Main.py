import re
from difflib import SequenceMatcher
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Function to preprocess text
def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Function to compare files and calculate matched percentage
def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        data_file = preprocess(file1.read())
        data_file2 = preprocess(file2.read())

    matches = SequenceMatcher(None, data_file, data_file2).ratio()
    print(f"The plagiarized content is {matches * 100:.2f}%")

# Paths to the text files
file1_path = 'text1.txt'
file2_path = 'text2.txt'

# Compare the files
compare_files(file1_path, file2_path)
