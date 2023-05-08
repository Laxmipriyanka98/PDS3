import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# NLTK stop words can be downloaded (one only).
nltk.download('stopwords')

# Fill a pandas DataFrame using the CSV file.
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

# As a text corpus, extract the "OriginalTweet" column.
corpus = df['OriginalTweet']

# initialize the NLTK stop words
stop_words = set(stopwords.words('english'))

# Create a blank list at startup to store the tokens without stop words.
filtered_tokens = []

# Remove stop words from each tweet in the corpus iteratively.
for tweet in corpus:
  # Utilizing word_tokenize from NLTK, tokenize the tweet.
  tweet_tokens = word_tokenize(tweet)

# Remove stop words from the tokens in the current tweet.
filtered_tokens.extend([token for token in tweet_tokens if token.lower() not in stop_words])

# Print the filtered tokens
print(filtered_tokens)
