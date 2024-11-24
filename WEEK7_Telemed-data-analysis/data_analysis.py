import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the csv file
df = pd.read_csv('hospital_db.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display general info about the dataset
print("\nDataset Info:")
df.info()

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Clean the data
# Example: Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Handle missing values (dropping rows with missing values)
df = df.dropna()

# Basic Data Analysis
# Filter only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Calculate the correlation matrix for numeric columns
correlation_matrix = numeric_df.corr()

# Display the correlation matrix
print("\nCorrelation matrix for numeric columns:")
print(correlation_matrix)

# Data Visualizations
# Example: Histogram of a specific column (update 'patient_id' to a valid column name if needed)
plt.figure(figsize=(8, 6))
sns.histplot(df['patient_id'], kde=True)
plt.title('Histogram of Patient IDs')
plt.xlabel('Patient ID')
plt.ylabel('Frequency')
plt.show()


# Example: Boxplot for a categorical variable and a numeric column
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='patient_id', data=df)
plt.title('Boxplot of Patient ID by Gender')
plt.xlabel('Gender')
plt.ylabel('Patient ID')
plt.show()

# Findings and Observations
# Add meaningful observations based on your analysis
print("\nFindings:")
print("1. The correlation matrix only includes the 'patient_id' column as it is the only numeric field.")
print("2. The histogram of 'patient_id' shows its distribution. This field likely serves as an identifier and may not be analytically useful.")
print("3. Gender-based boxplot highlights how 'patient_id' values are distributed by gender.")

