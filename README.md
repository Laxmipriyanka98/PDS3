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

B-Bit

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

C-bit

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

D bit

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# Load the CSV file into a pandas DataFrame
df=pd.read_csv('C:/Users/priya/OneDrive/Desktop/Test Jupyter/Corona_NLP_test.csv')


# Extract the "OriginalTweet" column as a text corpus
corpus = df['OriginalTweet']

# Concatenate all tweets into a single string
text = ' '.join(corpus)

# Tokenize the text
tokens = word_tokenize(text)

# Join the tokens back into a single string
processed_text = ' '.join(tokens)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='pink').generate(processed_text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
