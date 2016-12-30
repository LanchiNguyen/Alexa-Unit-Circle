from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
	return "<b>poop!poop!poop!poop!"

@ask.launch
def start_skill():
	welcome_message = "hello penis friends wanna do some weed?"
	return question(welcome_message)

@ask.intent("YesIntent")
def yes_answer():
	reply = "What is the sine of pi?"
	return statement(reply)

@ask.intent("NoIntent")
def no_answer():
	reply = "well fuck you"
	return statement(reply)

# To make the app run., same for all Flask apps 
if __name__ == '__main__':
	app.run(debug=True)