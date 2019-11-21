from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unilux.db'
db=SQLAlchemy(app)

class cadastro(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/enviar', methods=('GET', 'POST'))
def enviar():
    form = cadastro()
    if form.validate_on_submit():
        return render_template('feed.html', form=form)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__== '__main__':
    app.run(debug=True) 