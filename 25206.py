from sys import stdin

grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

grade_and_score_sum=0
score_sum=0

for i in range(20):
    _, score, grade = stdin.readline().rstrip().split()

    if grade == "P":
        continue

    grade_and_score_sum += float(score) * grades[grade]
    score_sum += float(score)

print(f"{(grade_and_score_sum/score_sum):.6f}")