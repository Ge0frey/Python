import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Task 1: Load and Explore the Dataset
df = pd.read_csv('hospital_db.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Basic statistics for numeric columns
print("\nBasic Statistics (mean, std, min, max, etc.):")
print(df.describe())

# Group by gender and calculate the mean (numeric only)
# Select numeric columns for the mean calculation
numeric_columns = df.select_dtypes(include=['number']).columns
print("\nGroup by gender and compute mean (numeric only):")
grouped_by_gender = df[numeric_columns].groupby(df['gender']).mean()
print(grouped_by_gender)

# Group by language and calculate the mean (numeric only)
print("\nGroup by language and compute mean (numeric only):")
grouped_by_language = df[numeric_columns].groupby(df['language']).mean()
print(grouped_by_language)

# Task 3: Data Visualization
# Plot distribution of patient IDs
plt.figure(figsize=(10, 6))
sns.histplot(df['patient_id'], kde=True, bins=30)
plt.title('Distribution of Patient IDs')
plt.xlabel('Patient ID')
plt.ylabel('Frequency')
plt.show()

# Plot count of patients by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', data=df)
plt.title('Count of Patients by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Plot count of patients by language
plt.figure(figsize=(10, 6))
sns.countplot(x='language', data=df)
plt.title('Count of Patients by Language')
plt.xlabel('Language')
plt.ylabel('Count')
plt.show()

# Scatter plot (example: relationship between patient_id and date_of_birth)
# Convert 'date_of_birth' to string for plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='patient_id', y=df['date_of_birth'].astype(str))  
plt.title('Patient ID vs Date of Birth')
plt.xlabel('Patient ID')
plt.ylabel('Date of Birth')
plt.show()
