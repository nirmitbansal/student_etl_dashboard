import pandas as pd
import mysql.connector
import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/transformed_data.csv")

data = pd.read_csv(file_path)

print("DATA READY TO LOAD:")
print(data)

conn = mysql.connector.connect(
    host="localhost",
    user="nirmitbansal",
    password="nirmit2708",
    database="nirmitbansal"
)

cursor = conn.cursor()

for _, row in data.iterrows():
    values = (
        int(row["student_id"]),
        row["name"],
        row["course"],
        int(row["year"]),
        row["subject"],
        int(row["marks"]),
        row["grade"],
        int(row["total_classes"]),
        int(row["attended_classes"]),
        float(row["attendance_percentage"])
    )

    cursor.execute("""
        INSERT INTO student_performance 
        (student_id, name, course, year, subject, marks, grade, total_classes, attended_classes, attendance_percentage)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, values)

conn.commit()
conn.close()

print("✅ Data successfully loaded into MySQL!")
