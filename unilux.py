from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unilux.db'
app.config['SECRET_KEY'] = 'sbisabxouw2oboe3038308h0asjs'
db=SQLAlchemy(app)

class cadastroForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    form = cadastroForm()
    if form.validate_on_submit():
        user1 = User()
        user1.name = form.name.data
        db.session.add(user1)
        db.session.commit()
    return render_template('cadastro.html', form=form)
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__== '__main__':
    app.run(debug=True) 