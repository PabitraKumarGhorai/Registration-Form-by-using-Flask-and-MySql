from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#config db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'vistara'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['full_name']
        gender = userDetails['gender']
        age = userDetails['age']
        degree = userDetails['degree']
        email = userDetails['email']
        mobile_number = userDetails['mobile_number']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO record(full_name, gender, age, degree, email, mobile_number) VALUES(%s, %s, %s, %s, %s, %s)",(name, gender, age, degree, email, mobile_number))
        mysql.connection.commit()
        cur.close()
        return '<h1 align="center"> SUCCESS..<h1>'
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)