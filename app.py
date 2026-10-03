import streamlit as st

st.set_page_config(page_title="Student Management System")

st.title("🎓 Student Management System")

# Student data
students = [
    {
        "id": "166",
        "name": "Suraj Chakraborty",
        "course": "BCA",
        "semester": "5th",
        "marks": 425,
        "total": 500
    },
    {
        "id": "040",
        "name": "Arpita Das",
        "course": "BCA",
        "semester": "5th",
        "marks": 390,
        "total": 500
    },
    {
        "id": "101",
        "name": "Amit Sharma",
        "course": "BCA",
        "semester": "5th",
        "marks": 450,
        "total": 500
    }
]

# Search section
st.header("🔍 Search Student")

search = st.text_input("Enter Student ID or Name")

if st.button("Search"):

    found = False

    for student in students:

        if (search.lower() == student["id"].lower()
                or search.lower() == student["name"].lower()):

            percentage = (student["marks"] / student["total"]) * 100

            if percentage >= 80:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            st.success("Student Found!")

            st.subheader("Student Details")

            st.write("**Student ID:**", student["id"])
            st.write("**Name:**", student["name"])
            st.write("**Course:**", student["course"])
            st.write("**Semester:**", student["semester"])
            st.write("**Marks:**", student["marks"], "/", student["total"])
            st.write("**Percentage:**", percentage, "%")
            st.write("**Grade:**", grade)

            if percentage >= 40:
                st.success("Result: PASS")
            else:
                st.error("Result: FAIL")

            found = True
            break

    if not found:
        st.error("Student not found!")