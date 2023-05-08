# PDS3
# pip install pandas nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize

# Loading CSV file into a pandas DataFrame
path=os.getcwd()
print(path)

df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

corpus = df['OriginalTweet']
tokens = []

# Tokenize each tweet in the corpus by iterating over it
for tweet in corpus:

# Utilizing word_tokenize from nltk, tokenize the tweet.
  tweet_tokens = word_tokenize(tweet)

# Tokens from the current tweet should be added to the list.
tokens.extend(tweet_tokens)

# Print the tokens
print(tokens)

B-Bit

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

C-bit

import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize

# Fill a pandas DataFrame using the CSV file.
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')

#  Create a text corpus from the "OriginalTweet" column.
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

D bit

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# Open a pandas DataFrame and load the CSV file.
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')


# Create a text corpus from the "OriginalTweet" column.
corpus = df['OriginalTweet']

# Concatenate all tweets into a single string
text = ' '.join(corpus)

# Tokenize the text
tokens = word_tokenize(text)

# Concatenate the tokens into a single string.
processed_text = ' '.join(tokens)

# Build a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='pink').generate(processed_text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
