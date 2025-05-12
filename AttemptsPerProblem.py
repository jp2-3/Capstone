import pandas as pd

# Load the csv file
df = pd.read_csv('MainTable.csv')

# Clean data i.e. drop any blank cells in the csv (used to increase accuracy)
df['Attempt'] = pd.to_numeric(df['Attempt'], errors='coerce')
df['ProblemID'] = pd.to_numeric(df['ProblemID'], errors='coerce')
df = df.dropna(subset=['Attempt', 'ProblemID'])

# Group by the ProblemID feature and calculates mean/average number of attempts
avg_attempts_per_problem = df.groupby('ProblemID')['Attempt'].mean().reset_index()
avg_attempts_per_problem['Attempt'] = avg_attempts_per_problem['Attempt'].round(2)

# Display
print(avg_attempts_per_problem)
