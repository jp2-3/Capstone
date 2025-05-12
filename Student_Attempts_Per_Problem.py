import pandas as pd

# Load original data
df = pd.read_csv('MainTable.csv')

# Group by SubjectID and ProblemID and sum the attempts
attempts_summary = df.groupby(['SubjectID', 'ProblemID'])['Attempt'].sum().reset_index()
attempts_summary.rename(columns={'Attempt': 'TotalAttempts'}, inplace=True)

# Save to a new CSV
attempts_summary.to_csv('Student_Attempts_Per_Problem.csv', index=False)
print(f"Summary saved to 'Student_Attempts_Per_Problem.csv' with {len(attempts_summary)} rows.")
