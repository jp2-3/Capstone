import pandas as pd

# Load data
df = pd.read_csv('MainTable.csv')

# unique student IDs
unique_ids = df['SubjectID'].dropna().unique()

# Create a new DataFrame
student_df = pd.DataFrame({'SubjectID': unique_ids})

# Save to a new CSV
student_df.to_csv('StudentIDs.csv', index=False)
print(f"{len(unique_ids)} unique student IDs saved to StudentIDs.csv")
