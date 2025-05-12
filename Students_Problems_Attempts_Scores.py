import pandas as pd

# Load original data
df = pd.read_csv('MainTable.csv')

# Select only the desired columns
selected_columns = df[['SubjectID', 'ProblemID', 'Attempt', 'Score']]

# Clean data
selected_columns = selected_columns.dropna(subset=['SubjectID', 'ProblemID', 'Attempt', 'Score'])

# Save to a new CSV
selected_columns.to_csv('Students_Problems_Attempts_Scores.csv', index=False)
print(f"Filtered data saved to 'Students_Problems_Attempts_Scores.csv' with {len(selected_columns)} rows.")
