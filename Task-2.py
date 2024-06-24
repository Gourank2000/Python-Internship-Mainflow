import pandas as pd

# Sample data (replace with your actual data)
data = {'Name': ['Alice', 'Bob', None, 'Charlie', 'Bob', 'David'],
        'Age': [25, 30, None, 22, 30, None],
        'City': ['New York', 'Los Angeles', 'New York', None, 'Los Angeles', 'Chicago'],
        'Order Amount': [100, 200, None, 150, 250, 300]}

# Load data into a pandas DataFrame
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull().sum())  # Shows how many missing values per column

# Handle missing values (example: replace with mean for numeric columns)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)  # Replace with a placeholder for city

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# --- Data Manipulation Examples ---

# Filter data: Get all orders above $200 from Los Angeles
filtered_df = df[(df['Order Amount'] > 200) & (df['City'] == 'Los Angeles')]

# Sort data: Sort by name in ascending order, then by order amount in descending order
sorted_df = df.sort_values(by=['Name', 'Order Amount'], ascending=[True, False])

# Group data: Group by city and calculate total order amount per city
grouped_by_city = df.groupby('City')['Order Amount'].sum()

# Print cleaned and manipulated dataframes (optional)
print("\nCleaned Data:")
print(df)

print("\nFiltered Data:")
print(filtered_df)

print("\nSorted Data:")
print(sorted_df)

print("\nGrouped Data:")
print(grouped_by_city)