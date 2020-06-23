from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nix2008@localhost:5432/pothole_reporting'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = "pothole_report"
	id = db.Column(db.Integer, primary_key=True)
	email_ = db.Column(db.String(120), unique=True)
	pothole_type_ = db.Column(db.String)
	department_ = db.Column(db.String)
	address_ = db.Column(db.String)
	landmark_ = db.Column(db.String)
	comment_ = db.Column(db.String)

	def __init__(self, email_, pothole_type_, department_, address_, landmark_, comment_):
		self.email_ = email_
		self.pothole_type_ = pothole_type_
		self.department_ = department_
		self.address_ = address_
		self.landmark_ = landmark_
		self.comment_ = comment_

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success", methods=['GET', 'POST'])
def success():
	if request.method == 'POST':
		email = request.form["email_address"]
		pothole_type = request.form["pothole_type"]
		department = request.form["department_name"]
		add = request.form["address"]
		landmark = request.form["landmark"]
		comment = request.form["comment"]
		if db.session.query(Data).filter(Data.email_ == email).count() == 0:
			data = Data(email, pothole_type, department, add, landmark, comment)
			db.session.add(data)
			db.session.commit()
			print(email, pothole_type, department, add, landmark, comment)
			send_email(email, pothole_type, department, add, landmark, comment)
			return render_template("success.html")
	return render_template("index.html", text="Already got request from this email.")

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)















