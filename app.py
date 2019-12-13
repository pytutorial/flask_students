from flask import Flask, request, render_template, redirect

app = Flask(__name__)

students = [
    {'id' : 1, 'studentNo': '10001', 'name': 'Student 1'},
    {'id' : 2, 'studentNo': '10002', 'name': 'Student 2'},
]

@app.route('/')
def index():
    return render_template('index.html', 
            students=students)

@app.route('/create_student')
def createStudent():
    return render_template(
        'student_form.html')

@app.route('/save_student',methods=['POST'])
def saveStudent():
    student = dict(request.form)
    if len(students) == 0:
        student['id'] = 1
    else:
        student['id'] = 1+students[-1]['id']
    
    students.append(student)
    return redirect('/')        

app.run(debug=True)

# new