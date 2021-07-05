from flask import Flask,render_template,request,flash,url_for,redirect
import sqlite3

#get db connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.secret_key = "employee_crud"
@app.route('/')
def Index():
    conn = get_db_connection()
    data = conn.execute("select * from Employee").fetchall()

    return render_template('index.html',employee = data)

@app.route('/add_emp',methods=['POST'])
def add_employee():
    conn = get_db_connection()
    if request.method == 'POST':
        Name = request.form['Name']
        Designation = request.form['Designation']
        Address = request.form['Address']
        Phone = request.form['Phone']
        conn.execute("INSERT INTO employee (Name, Designation, Address, Phone) VALUES (?,?,?,?)", (Name, Designation, Address, Phone))
        conn.commit()
        flash("Employee Added Successfully")
        return redirect(url_for('Index'))


@app.route('/edit/<Name>', methods=['POST', 'GET'])
def get_employee(Name):
    conn = get_db_connection()

    data = conn.execute('SELECT * FROM Employee WHERE Name = ?', (Name,)).fetchall()

    conn.close()
    print(data[0])
    return render_template('update.html', Employee=data[0])

@app.route('/update/<Name>',methods= ['POST'])
def update_employee(Name):
    conn = get_db_connection()
    if request.method == "POST":
        Designation = request.form['Designation']
        Address = request.form['Address']
        Phone = request.form['Phone']
        conn.execute("update Employee set Designation=?,Address=?,Phone=? where Name=?",(Designation,Address,Phone,Name))
        conn.commit()
        flash("Employee updated successfully")
        return redirect(url_for('Index'))

@app.route('/delete/<Name>',methods=['POST','GET'])
def delete_employee(Name):
    conn = get_db_connection();

    conn.execute("delete from Employee where Name=?",(Name,))
    conn.commit()
    flash("Employee deleted Successfully")
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run()