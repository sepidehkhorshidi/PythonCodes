import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Read the CSV file and store it in a pandas dataframe
df = pd.read_csv('file_name.csv')

# Concatenate all text columns into a single string
text = ' '.join(df['text_column'])

# Tokenize the text into words and sentences
words = word_tokenize(text)
sentences = sent_tokenize(text)

# Remove stop words from the words list
stop_words = set(stopwords.words('english'))
words_filtered = [word for word in words if not word.lower() in stop_words]

# Stem or lemmatize the words
stemmer = PorterStemmer()
words_stemmed = [stemmer.stem(word) for word in words_filtered]

lemmatizer = WordNetLemmatizer()
words_lemmatized = [lemmatizer.lemmatize(word) for word in words_filtered]

# Calculate word frequency
freq = nltk.FreqDist(words_stemmed)
freq.plot(20, cumulative=False)

# Perform Part-of-Speech (POS) tagging on the text
pos_tags = nltk.pos_tag(words_filtered)

# Print the POS tags of the first 10 words
print(pos_tags[:10])