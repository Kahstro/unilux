from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unilux.db'
app.config['SECRET_KEY'] = 'sbisabxouw2oboe3038308h0asjs'
db=SQLAlchemy(app)

class cadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    sobrenome = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.nome

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    form = cadastroForm()
    if form.validate_on_submit():
        user1 = User()
        user1.nome = form.nome.data
        user1.sobrenome = form.sobrenome.data
        user1.email = form.email.data
        user1.senha = form.senha.data
        db.session.add(user1)
        db.session.commit()
    return render_template('cadastro.html', form=form)
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__== '__main__':
    app.run(debug=True) 