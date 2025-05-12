import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_csv = "MainTable.csv"
df = pd.read_csv(input_csv)

avg_attempts = df.groupby('X-ExerciseID')['Attempt'].mean().reset_index()
avg_attempts.rename(columns={'Attempt': 'AverageAttempts'}, inplace=True)

output_csv = ("average_attempts.csv")
avg_attempts.to_csv(output_csv, index=False)

print(f"data saved to {output_csv}")