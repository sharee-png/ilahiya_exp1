from flask import *
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///emp.db'
app.config['SECRET_KEY']='abc'

db=SQLAlchemy(app)

class Employees(db.Model):
    id=db.Column('employee_id',db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address

@app.route('/add',methods=['GET','POST'])
def add_emp():
    if request.method=="POST":
        emp=Employees(request.form['name'],request.form['add'])
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('display'))
    else:
        return render_template('add.html')

@app.route('/')   
def display():
    return render_template('listemp.html',emp=Employees.query.all())

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)