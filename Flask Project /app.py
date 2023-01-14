from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class todo(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable= False)
    desc = db.Column(db.String(500), nullable= False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
    
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print ("post request is working")
        title =  (request.form['title'])
        desc = (request.form['desc'])
        todolist = todo(title = title, desc = desc)
        db.session.add(todolist)
        db.session.commit()
    
    return render_template('index.html', alltodo = todo.query.all())
    # return 'Hello, World!'

@app.route('/show')
def products():
    print (todo.query.all())
    return 'This is the products page'

@app.route('/update/<int:sno>',  methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
    
        title =  (request.form['title'])
        desc = (request.form['desc'])
        todo_upd = todo.query.filter_by(sno=sno).first()
        todo_upd.title = title
        todo_upd.desc = desc
        db.session.add(todo_upd)
        db.session.commit()
        return redirect('/')
    todo_upd = todo.query.filter_by(sno=sno).first()
    return render_template('/update.html', todos = todo_upd)

@app.route('/delete/<int:sno>', methods = ['GET', 'POST'])
def delete(sno):
    del_sno = todo.query.filter_by(sno=sno).first()
    db.session.delete(del_sno)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    
    app.run(debug=True)
    