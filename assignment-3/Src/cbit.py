import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize

# Load the CSV file into a pandas DataFrame
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

# Extract the "OriginalTweet" column as a text corpus
corpus = df['OriginalTweet']

# Initialize an empty list to store the tokens
tokens = []

# Iterate over each tweet in the corpus and tokenize it
for tweet in corpus:
  # Tokenize the tweet using word_tokenize from NLTK
  tweet_tokens = word_tokenize(tweet)

# Add the tokens of the current tweet to the list
tokens.extend(tweet_tokens)

# Count the word frequencies
word_frequencies = Counter(tokens)

# Print the word frequencies
for word, frequency in word_frequencies.items():
  print(f'{word}: {frequency}')