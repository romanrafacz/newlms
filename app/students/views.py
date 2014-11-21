from flask import render_template, Blueprint, redirect, request
from app.students.form import StudentForm

from app import db
from app.models import Students

students_blueprint = Blueprint(
        'students', __name__,
        template_folder = "templates"
        )

@students_blueprint.route('/students')
def students():
    ###Initialize Form
    form = StudentForm()
    students = db.session.query(Students).all()
    return render_template("index.html", form=form, students=students)

@students_blueprint.route('/addstudent', methods=['POST', 'GET'])
def addstudent():
        if request.method == 'POST':
            db.session.add(Students(first_name=request.form['first_name'], last_name=request.form['last_name'], email=request.form['email'], phone=request.form['phone']))
            db.session.commit()
            return redirect('students')

        return redirect('students')
