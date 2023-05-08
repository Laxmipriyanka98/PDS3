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