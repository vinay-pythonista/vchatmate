from flask import Flask, render_template

from wtform_fields import *
from models import *

app = Flask(__name__)

app.secret_key = 'your secret key'


#Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://chyebunskgtkrc:6528a999df885f18da144d2bd4b0a8892d5fe9ab7c147133af1278c9170b887f@ec2-34-236-215-156.compute-1.amazonaws.com:5432/dbr9jepd862r5h'

db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():

	reg_form = RegistrationForm()

	if reg_form.validate_on_submit():
		username = reg_form.username.data
		password = reg_form.password.data

		# Check username exists
		user_object = User.query.filter_by(username=username).first()
		if user_object:
			return "Username is already taken!"

		# Add user to DB
		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()
		return "User successfully registered!"

	return render_template("index.html", form=reg_form)

if __name__ == "__main__":

	app.run(debug=True)