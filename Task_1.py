import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("D:/Data Analytics/Techno_Hacks/Task_1.csv")
print("Given Data Set\n",df)
print("No of columns in original set\n",df.count())
print("Number of null values in each column\n",df.isnull().sum())
df=df.dropna()
print("Data set after removing the null values\n",df)
print(df.count())

fare_data = df['Fare']
plt.boxplot(fare_data)
plt.title('Box Plot of Fare')
plt.ylabel('Fare')
plt.show()

from scipy import stats
z_scores = stats.zscore(fare_data)
threshold = 2
df = df[z_scores > threshold]
print(df)
plt.boxplot(df['Fare'])


'''import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv("D:/Data Analytics/Techno_Hacks/train.csv")

# Step 1: Data Exploration
print("Step 1: Data Exploration")
print("=======================================")

# Display the original dataset
print("Original Dataset Overview:")
print(df.head())

# Count the number of rows and columns in the dataset
num_rows, num_columns = df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)

# Step 2: Data Cleaning
print("\nStep 2: Data Cleaning")
print("=======================================")

# Remove rows with missing values
df_cleaned = df.dropna()

# Display the cleaned dataset
print("Cleaned Dataset Overview:")
print(df_cleaned.head())

# Step 3: Data Analysis
print("\nStep 3: Data Analysis")
print("=======================================")

# Extract 'Fare' data for analysis
fare_data = df_cleaned['Fare']

# Create a box plot for 'Fare'
plt.boxplot(fare_data)
plt.title('Box Plot of Fare')
plt.ylabel('Fare')
plt.show()

# Calculate Z-scores for 'Fare'
z_scores = stats.zscore(fare_data)

# Set a threshold for identifying outliers
threshold = 2

# Filter out rows with Z-scores greater than the threshold
df_no_outliers = df_cleaned[z_scores <= threshold]

# Display the dataset after removing outliers
print("Dataset After Removing Outliers:")
print(df_no_outliers.head())

# Create a box plot for 'Fare' after removing outliers
plt.boxplot(df_no_outliers['Fare'])
plt.title('Box Plot of Fare (Outliers Removed)')
plt.ylabel('Fare')
plt.show()

# Step 4: Conclusion
print("\nStep 4: Conclusion")
print("=======================================")

# Provide a summary or conclusion of the analysis
print("Data analysis and cleaning completed. Outliers have been removed.")
'''