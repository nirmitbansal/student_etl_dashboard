import pandas as pd
import os

base_path = os.path.dirname(__file__)

students = pd.read_csv(os.path.join(base_path, "../data/students.csv"))
marks = pd.read_csv(os.path.join(base_path, "../data/marks.csv"))
attendance = pd.read_csv(os.path.join(base_path, "../data/attendance.csv"))

merged = pd.merge(students, marks, on="student_id")
merged = pd.merge(merged, attendance, on="student_id")

merged["attendance_percentage"] = (merged["attended_classes"] / merged["total_classes"]) * 100

def assign_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

merged["grade"] = merged["marks"].apply(assign_grade)

output_path = os.path.join(base_path, "../data/transformed_data.csv")
merged.to_csv(output_path, index=False)

print("✅ Transformed data saved to data/transformed_data.csv")
