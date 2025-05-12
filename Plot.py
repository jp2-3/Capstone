import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
input_csv = "average_attempts.csv"  # Ensure correct file name
df = pd.read_csv(input_csv)

# Sort by 'AverageAttempts' for better visualization
df = df.sort_values(by='AverageAttempts', ascending=False)

# Create a bar chart
plt.figure(figsize=(40, 40))
plt.bar(df['X-ExerciseID'].astype(str), df['AverageAttempts'], color='skyblue')

# Labels and title
plt.xlabel("Exercise ID", fontsize=12)  # Fixed typo here
plt.ylabel("Average Attempts", fontsize=12)
plt.title("Average Attempts per Exercise", fontsize=14)
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

# Adjust layout and show plot
plt.tight_layout()
plt.show()

unique_exercises = df['X-ExerciseID'].unique()

total_unique_exercises = len(unique_exercises)
print("Unique Exercise IDs:")
print(unique_exercises)
print(f"Total number of unique Exercise IDs: {total_unique_exercises}")
