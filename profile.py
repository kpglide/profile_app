from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.update(
	SERVER_NAME = 'localhost:8080'
)

username = 'Kevin Glidewell'

@app.route('/home')
def main():
	message = "Hi, this is %s's website.  Please look around." % username
	return render_template('home.html', username=username, message=message)
	
@app.route('/hobbies')
def hobbies():
	hobbies = 'golf, guitar and python'
	return render_template('hobbies.html', hobbies_list=hobbies, username=username)
	
@app.route('/family')
def family():	
	family_members = 'Jill, Zoe, Gouda and Gibson'
	return render_template('family.html', family=family_members, username=username)

if __name__ == "__main__":
	app.run(debug=True)
	
	