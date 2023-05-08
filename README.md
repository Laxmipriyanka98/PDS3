# PDS3
# pip install pandas nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize

# Load the CSV file into a pandas DataFrame
path=os.getcwd()
print(path)

df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

corpus = df['OriginalTweet']

tokens = []

# Iterate over each tweet in the corpus and tokenize it
for tweet in corpus:
  # Tokenize the tweet using word_tokenize from nltk
  tweet_tokens = word_tokenize(tweet)

# Add the tokens of the current tweet to the list
tokens.extend(tweet_tokens)

# Print the tokens
print(tokens)
