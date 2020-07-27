from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,URL
from wtforms import ValidationError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

class Home(FlaskForm):
	link = StringField('paste the link here', validators=[DataRequired(), URL(message='Must be a valid URL')])
	submit=SubmitField('Predict')







@app.route('/',methods=['GET','POST'])
def index():
	form = Home()
	if form.validate_on_submit():
		return render_template('home.html',output='hi',form=form)
	elif request.method=='GET':
		return render_template('home.html',output='',form=form)


if __name__=='__main__':
	app.run(debug=True)