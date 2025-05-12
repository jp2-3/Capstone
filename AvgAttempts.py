
import pandas as pd

df = pd.read_csv('MainTable.csv')

def get_studentAVG_per_problem(SubjectID, ProblemID):
    filtered = df[(df['SubjectID'] == SubjectID) & (df['ProblemID'] == ProblemID)]

    if filtered.empty:
        return f'No data for student id {SubjectID} No data for problem id {ProblemID}'

    return float(filtered['Attempt'].mean())

def get_avgScore_per_problem(SubjectID, ProblemID):
    filtered = df[(df['SubjectID'] == SubjectID) & (df['ProblemID'] == ProblemID)]

    if filtered.empty:
        return f'No data for student id {SubjectID} No data for problem id {ProblemID}'

    return float(filtered['Score'].mean())

SubjectID = int(input('Enter Subject ID: '))

while True:
    problem_input = input("Enter problem ID or type q to quit: ")

    if problem_input == "q" or problem_input == "Q":
        print('Quitting...')
        break

    try:
        ProblemID = int(problem_input)

        average = get_studentAVG_per_problem(SubjectID, ProblemID)
        avg_score = get_avgScore_per_problem(SubjectID, ProblemID)

        print(f"Average Attempts: {average:.2f}")
        print(f"Average Score: {avg_score:.2f}")


    except ValueError:
        print("Please enter a valid numeric Problem ID.\n")

