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