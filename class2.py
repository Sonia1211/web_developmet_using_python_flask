from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint
from db import Register,Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager,current_user,login_user,logout_user,login_required




"""Here the current module is main"""
app=Flask(__name__)
app.secret_key='sa'
engine=create_engine('sqlite:///register.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
	return session.query(User).get(int(user_id))

@login_required
@app.route('/show')
def showData():
	register1=session.query(Register).all()
	return render_template('show.html',reg=register1)

@app.route('/add',methods=['POST','GET'])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],email=request.form['email'],des=request.form['des'])
		session.add(newData)
		session.commit()
		flash("New data is added")
		return redirect(url_for('showData'))
	else:
		return render_template('add.html')

@app.route('/edit/<int:register_id>',methods=['POST','GET'])
def editData(register_id):
	editeddata=session.query(Register).filter_by(id=register_id).one()
	if request.method=='POST':
		editeddata.id=request.form['id']
		editeddata.name=request.form['name']
		editeddata.email=request.form['email']
		editeddata.des=request.form['des']
		session.add(editeddata)
		session.commit()
		flash("Data is edited")
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editeddata)

@app.route('/<int:register_id>/delete',methods=['POST','GET'])
def deleteData(register_id):
	deleteddata=session.query(Register).filter_by(id=register_id).one()
	if request.method=='POST':
		session.delete(deleteddata)
		session.commit()
		flash("Data is deleted...!!!")
		return redirect(url_for('showData'))
	else:
		return render_template('delete.html',register=deleteddata)

@app.route('/register',methods=['POST','GET'])
def registerData():
	if request.method=='POST':
		regdata=User(name=request.form['name'],email=request.form['email'],password=request.form['password'])
		session.add(regdata)
		session.commit()
		return redirect(url_for('login'))
	else:
		return render_template('register.html')
@app.route('/index',methods=['POST','GET'])
def index():
	return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('showData'))
	try:
		if request.method=='POST':
			user=session.query(User).filter_by(email=request.form['email'],password=request.form['password']).first()
			if user:
				login_user(user)
				return redirect(url_for('showData'))
			else:
				flash('Login failed')
		else:
			return render_template('login.html',title='login')
	except Exception as e:
		flash("Login Failed")
	else:
		return render_template('login.html',title='login')
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('index'))










"""
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='specialsony8899@gmail.com'
app.config['MAIL_PASSWORD']='Sony@1708'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
otp=randint(000000,999999)
app.secret_key='df'

@app.route('/email')
def email():
	return render_template('email.html')
@app.route('/email_verify',methods=['POST','GET'])
def verify():
	email=request.form['mail']
	msg=Message('OTP for verification',sender='specialsony8899@gmail.com', recipients=[email])
	msg.body=str(otp)
	mail.send(msg)
	return render_template('email_verify.html')
@app.route('/validation',methods=['POST','GET'])
def validation():
	user_otp=request.form['otpvalue']
	if otp==int(user_otp):
		return "OTP verification is done"
	else:
		return "Invalid OTP"""














"""@app.route('/home')
def index():
	return "<h1>p3t3rp4rk3r.....Sonia.....Papa</h1>"
@app.route('/index/<name>')
def ind(name):
	return "<h1>This is index page<h1> "+name
@app.route('/home/<int:age>/<name>')
def ag(name,age):
	return "Name{} age{}".format(name,age)
#Function Mapping
@app.route('/admin')
def admin():
	return "<h1>This is admin page</h1>"
@app.route('/student')
def student():
	return "<h1>This is Student page</h1>"
@app.route('/home/<name>')
def home(name):
	if name=='admin':
		return redirect(url_for('admin'))
	if name=='student':
		return redirect(url_for('student'))
#File Access
@app.route('/login/')
def login1():
	return render_template('login.html')

#adding html route name to html page
#@app.route('/login/<name>')
#def login(name):
	#return render_template('login.html',username=name)
#table adding
@app.route('/table/<int:value>')
def table(value):
	return render_template('login.html',value1=value)

@app.route('/upload')
def upload():
	return render_template("upload.html")

@app.route('/success',methods=['POST','GET'])
def success():
	if request.method=='POST':
		f=request.files['image']
		f.save(f.filename)
		return render_template('success.html',name=f.filename)
	else:
		return "Please Check code"













"""










if __name__=='__main__':
	app.run(debug=True)