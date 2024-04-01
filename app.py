from flask import Flask, render_template, request, redirect
import mysql.connector
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="registration_db"
)
cursor = db.cursor()

# Root endpoint
@app.route('/')
def index():
    return render_template('register.html')

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Get form data
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        # Hash password
        password = sha256_crypt.hash(request.form['password'])
        
        # Insert data into database
        query = "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
