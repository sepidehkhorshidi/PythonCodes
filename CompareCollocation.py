import pandas as pd
import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords

# Read the CSV file and store it in a pandas dataframe
df = pd.read_csv('file_name.csv')

# Concatenate all text columns into a single string
text = ' '.join(df['text_column'])

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stop words from the words list
stop_words = set(stopwords.words('english'))
words_filtered = [word for word in words if not word.lower() in stop_words]

# Calculate bigram collocations of a word
word = 'your_word_here'
bigram_measures = BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words_filtered)
finder.apply_word_filter(lambda w: w.lower() in stop_words)
collocations = finder.nbest(bigram_measures.pmi, 10)
collocations_filtered = [col for col in collocations if word in col]

# Print the collocations of the word
print(f"Collocations of '{word}':")
for col in collocations_filtered:
    print(col)