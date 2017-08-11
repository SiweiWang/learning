# Simple web app that adds and displays list of students

from flask import Flask, render_template, redirect, request, url_for

from python.student.student import Student
students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        student_id = request.form.get("student-id", "")
        student_name = request.form.get("name", "")
        student_school_name = request.form.get("school-name", "")

        new_student = Student(name=student_name, student_id=student_id, school_name=student_school_name)
        students.append(new_student)

        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)