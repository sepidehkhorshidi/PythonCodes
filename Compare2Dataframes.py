import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files and store them in pandas dataframes
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Compare the number of rows and columns in the two dataframes
if df1.shape == df2.shape:
    print("The two dataframes have the same shape.")
else:
    print("The two dataframes have different shapes.")

# Compare the mean of a column in the two dataframes
mean1 = df1['column_name'].mean()
mean2 = df2['column_name'].mean()

if mean1 > mean2:
    print("The mean of column_name is higher in file1.")
else:
    print("The mean of column_name is higher in file2.")

# Create a bar chart of a column in both dataframes for comparison
plt.bar(df1['column_name'], label='File 1')
plt.bar(df2['column_name'], label='File 2')
plt.legend()
plt.show()

# Create a scatter plot of two columns in both dataframes for comparison
plt.scatter(df1['column_name1'], df1['column_name2'], label='File 1')
plt.scatter(df2['column_name1'], df2['column_name2'], label='File 2')
plt.legend()
plt.show()