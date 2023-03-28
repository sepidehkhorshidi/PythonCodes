import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in a pandas dataframe
df = pd.read_csv('file_name.csv')

# Display the first 5 rows of the dataframe
print(df.head())

# Display summary statistics of the dataframe
print(df.describe())

# Display the count of each unique value in a column of the dataframe
print(df['column_name'].value_counts())

# Create a bar chart of the count of each unique value in a column of the dataframe
df['column_name'].value_counts().plot(kind='bar')
plt.show()

# Create a scatter plot of two columns of the dataframe
df.plot(x='column_name1', y='column_name2', kind='scatter')
plt.show()

# Create a histogram of a column of the dataframe
df['column_name'].plot(kind='hist')
plt.show()

# Create a box plot of a column of the dataframe
df['column_name'].plot(kind='box')
plt.show()