import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize

# Fill a pandas DataFrame using the CSV file.
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

# Create a text corpus from the "OriginalTweet" column.
corpus = df['OriginalTweet']

# Create a blank list to hold the tokens.
tokens = []

# Tokenize each tweet in the corpus by iterating over it
for tweet in corpus:
  # Utilizing word_tokenize from NLTK, tokenize the tweet.
  tweet_tokens = word_tokenize(tweet)

# Add the current tweet's tokens to the list.
tokens.extend(tweet_tokens)

# Determine the word frequency.
word_frequencies = Counter(tokens)

# Print the word frequencies
for word, frequency in word_frequencies.items():
  print(f'{word}: {frequency}')