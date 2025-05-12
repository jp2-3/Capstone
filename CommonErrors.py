import pandas as pd

# load the CSV file MainTable.csv
df = pd.read_csv("MainTable.csv", dtype={'CompileMessageData': str})

# ensure that the 'CompileMessageData' feature is treated as a string
df['CompileMessageData'] = df['CompileMessageData'].astype(str).str.strip()

# ensuring invalid data isnt used
valid_data = df[
    (df['CompileMessageData'].notna()) &
    (df['CompileMessageData'].str.lower().isin(['nan', 'none', ''])) == False
]

# select features 'ProblemID' and 'CompileMessageData'
error_data = valid_data[['ProblemID', 'CompileMessageData']].copy()

# Save to a new CSV file
output_csv = "problem_errors_filtered.csv"
error_data.to_csv(output_csv, index=False)

print(f"Data saved successfully to {output_csv}")

