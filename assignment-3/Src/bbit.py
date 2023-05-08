import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stop words (only needed once)
nltk.download('stopwords')

# Load the CSV file into a pandas DataFrame
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

# Extract the "OriginalTweet" column as a text corpus
corpus = df['OriginalTweet']

# Initialize stop words from NLTK
stop_words = set(stopwords.words('english'))

# Initialize an empty list to store the tokens without stop words
filtered_tokens = []

# Iterate over each tweet in the corpus and remove stop words
for tweet in corpus:
  # Tokenize the tweet using word_tokenize from NLTK
  tweet_tokens = word_tokenize(tweet)

# Remove stop words from the current tweet's tokens
filtered_tokens.extend([token for token in tweet_tokens if token.lower() not in stop_words])

# Print the filtered tokens
print(filtered_tokens)