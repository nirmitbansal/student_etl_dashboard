import streamlit as st
import pandas as pd
import altair as alt

st.markdown("""
# 🎓 Student Performance Analytics Dashboard  
### Real-Time Academic Insights Powered by ETL & MySQL
""")

df = pd.read_csv("data/transformed_data.csv")

st.subheader("🎛 Filters")

course_filter = st.selectbox(
    "Select Course",
    options=["All"] + list(df["course"].unique())
)

subject_filter = st.selectbox(
    "Select Subject",
    options=["All"] + list(df["subject"].unique())
)

grade_filter = st.selectbox(
    "Select Grade",
    options=["All"] + list(df["grade"].unique())
)

# Apply filters
filtered_df = df.copy()

if course_filter != "All":
    filtered_df = filtered_df[filtered_df["course"] == course_filter]

if subject_filter != "All":
    filtered_df = filtered_df[filtered_df["subject"] == subject_filter]

if grade_filter != "All":
    filtered_df = filtered_df[filtered_df["grade"] == grade_filter]

st.markdown("## 📌 Executive Summary")


st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Average Marks", round(df["marks"].mean(), 2))
col3.metric("Average Attendance %", round(df["attendance_percentage"].mean(), 2))
col4.metric("Fail Count", len(df[df["grade"] == "F"]))

st.subheader("📋 Student Data")
st.dataframe(df)

st.markdown("## 📊 Performance Analytics")


st.subheader("📊 Average Marks by Subject")
avg_marks = df.groupby("subject")["marks"].mean()
st.bar_chart(avg_marks)

st.subheader("🎓 Grade Distribution")
grade_count = df["grade"].value_counts()
st.bar_chart(grade_count)

st.subheader("⚠️ Students with Low Attendance")
low_attendance = df[df["attendance_percentage"] < 75]
st.dataframe(low_attendance)

st.subheader("🔍 Search Student")
student_name = st.text_input("Enter student name")

if student_name:
    result = df[df["name"].str.contains(student_name, case=False)]
    st.dataframe(result)

st.markdown("## 🏆 Student Rankings")

st.subheader("🏆 Top Performing Students")

top_students = (
    filtered_df.groupby(["student_id", "name"])["marks"]
    .mean()
    .reset_index()
    .sort_values(by="marks", ascending=False)
)

top_students["Rank"] = range(1, len(top_students) + 1)

st.dataframe(top_students)

st.markdown("## ⚠️ Academic Risk Monitor")

st.subheader("⚠️ At-Risk Students")

at_risk = filtered_df[
    (filtered_df["attendance_percentage"] < 75) |
    (filtered_df["marks"] < 40)
]

if len(at_risk) > 0:
    st.warning("These students need attention")
    st.dataframe(at_risk)
else:
    st.success("No students at risk 🎉")
