# pip install pandas nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize

# Load CSV file into a pandas DataFrame
path=os.getcwd()
print(path)

df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

corpus = df['OriginalTweet']

tokens = []

# Tokenize each tweet in the corpus by iterating over it
for tweet in corpus:
  # Utilizing word_tokenize from nltk, tokenize the tweet
  tweet_tokens = word_tokenize(tweet)

# Tokens from the current tweet should be added to the list.
tokens.extend(tweet_tokens)

# Print the tokens
print(tokens)
