import pandas as pd
import os

base_path = os.path.dirname(__file__)

students = pd.read_csv(os.path.join(base_path, "../data/students.csv"))
marks = pd.read_csv(os.path.join(base_path, "../data/marks.csv"))
attendance = pd.read_csv(os.path.join(base_path, "../data/attendance.csv"))

print("STUDENTS DATA")
print(students)

print("\nMARKS DATA")
print(marks)

print("\nATTENDANCE DATA")
print(attendance)
