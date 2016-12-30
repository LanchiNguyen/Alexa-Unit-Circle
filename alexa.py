from flask import Flask
from flask_ask import Ask, statement, question, session
import random

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
	return "<b>poop!poop!poop!poop!"

@ask.launch
def start_skill():
	welcome_message = "Are you ready to do some math?"
	return question(welcome_message)

@ask.intent("YesIntent")
def generate_question():
	questions = ["What is the Cosine of two pi",
	"What is the sine of two pi",
	"What is the tangent of two pi",
	"What is the secant of two pi",
	"What is the cosecant of two pi",
	"What is the cotangent of two pi",
	"What is the cosine of pi over six",
	"What is the sine of pi over six",
	"What is the tangent of pi over six",
	"What is the secant of pi over six",
	"What is the cosecant of pi over six",
	"What is the cotangent of pi over six",
	"What is the cosine of pi over four",
	"What is the sine of pi over four",
	"What is the tangent of pi over four",
	"What is the secant of pi over four",
	"What is the cosecant of pi over four",
	"What is the cotangent of pi over four",
	"What is the cosine of pi over three",
	"What is the sine of pi over three",
	"What is the tangent of pi over three",
	"What is the secant of pi over three",
	"What is the cosecant of pi over three",
	"What is the cotangent of pi over three",
	"What is the cosine of pi over two",
	"What is the sine of pi over two",
	"What is the tangent of pi over two",
	"What is the secant of pi over two",
	"What is the cosecant of pi over two",
	"What is the cotangent of pi over two",
	"What is the cosine of five pi over six",
	"What is the sine of five pi over six",
	"What is the tangent of five pi over six",
	"What is the secant of five pi over six",
	"What is the cosecant of five pi over six",
	"What is the cotangent of five pi over six",
	"What is the cosine of three pi over four",
	"What is the sine of three pi over four",
	"What is the tangent of three pi over four",
	"What is the secant of three pi over four",
	"What is the cosecant of three pi over four",
	"What is the cotangent of three pi over four",
	"What is the cosine of two pi over three",
	"What is the sine of two pi over three",
	"What is the tangent of two pi over three",
	"What is the secant of two pi over three",
	"What is the cosecant of two pi over three",
	"What is the cotangent of two pi over three",
	"What is the cosine of pi",
	"What is the sine of pi",
	"What is the tangent of pi",
	"What is the secant of pi",
	"What is the cosecant of pi",
	"What is the cotangent of pi",
	"What is the cosine of seven pi over six",
	"What is the sine of seven pi over six",
	"What is the tangent of seven pi over six",
	"What is the secant of seven pi over six",
	"What is the cosecant of seven pi over six",
	"What is the cotangent of seven pi over six",
	"What is the cosine of five pi over four",
	"What is the sine of five pi over four",
	"What is the tangent of five pi over four",
	"What is the secant of five pi over four",
	"What is the cosecant of five pi over four",
	"What is the cotangent of five pi over four",
	"What is the cosine of four pi over three",
	"What is the sine of four pi over three",
	"What is the tangent of four pi over three",
	"What is the secant of four pi over three",
	"What is the cosecant of four pi over three",
	"What is the cotangent of four pi over three",
	"What is the cosine of three pi over two",
	"What is the sine of three pi over two",
	"What is the tangent of three pi over two",
	"What is the secant of three pi over two",
	"What is the cosecant of three pi over two",
	"What is the cotangent of three pi over two",
	"What is the cosine of eleven pi over six",
	"What is the sine of eleven pi over six",
	"What is the tangent of eleven pi over six",
	"What is the secant of eleven pi over six",
	"What is the cosecant of eleven pi over six",
	"What is the cotangent of eleven pi over six",
	"What is the cosine of seven pi over four",
	"What is the sine of seven pi over four",
	"What is the tangent of seven pi over four",
	"What is the secant of seven pi over four",
	"What is the cosecant of seven pi over four",
	"What is the cotangent of seven pi over four",
	"What is the cosine of five pi over three",
	"What is the sine of five pi over three",
	"What is the tangent of five pi over three",
	"What is the secant of five pi over three",
	"What is the cosecant of five pi over three",
	"What is the cotangent of five pi over three",]

	answers = ["one",
	"zero",
	"zero",
	"one",
	"undefined",
	"undefined",
	"root three over two",
	"one half",
	"one over root three",
	"two over root three",
	"two",
	"root three",
	"root two over two",
	"root two over two",
	"one",
	"two over root two",
	"two over root two",
	"one",
	"one half",
	"root three over two",
	"root three",
	"two",
	"two over root three",
	"one over root three",
	"zero",
	"one",
	"undefined",
	"undefined",
	"one",
	"zero",
	"negative root three over two",
	"one half",
	"negative one over root three",
	"negative two over root three",
	"two",
	"negative root three",
	"negative root two over two",
	"root two over two",
	"negative one",
	"negative two over root two",
	"two over root two",
	"negative one",
	"negative one half",
	"root three over two",
	"negative root three",
	"negative two",
	"two over root three",
	"negative one over root three",
	"negative one",
	"zero",
	"zero",
	"negative one",
	"undefined",
	"undefined",
	"negative root three over two",
	"negative one half",
	"one over root three",
	"negative two over root three",
	"negative two",
	"root three",
	"negative root two over two",
	"negative root two over two",
	"one",
	"negative two over root two",
	"negative two over root two",
	"one",
	"negative one half",
	"negative root three over two",
	"root three",
	"negative two",
	"negative two over root three",
	"one over root three",
	"zero",
	"negative one",
	"undefined",
	"undefined",
	"negative one",
	"zero",
	"root three over two",
	"negative one half",
	"negative one over root three",
	"two over root three",
	"negative two",
	"negative root three",
	"root two over two",
	"negative root two over two",
	"negative one",
	"two over root two",
	"negative two over root two",
	"negative one",
	"one half",
	"negative root three over two",
	"negative root three",
	"two",
	"negative two over root three",
	"negative one over root three",]

	index =  random.randint(0, 95)
	session.attributes['correct'] = answers[index]
	return question(questions[index])

@ask.intent("AnswerIntent")
def answer(their_answer):
	correct_answer = session.attributes['correct']
	if their_answer == correct_answer:
		return question("Smart baby. Wanna continue?")
	else:
		return question("Are you a retard? Try another one?")

@ask.intent("NoIntent")
def no_answer():
	reply = "well fuck you"
	return statement(reply)

# To make the app run., same for all Flask apps 
if __name__ == '__main__':
	app.run(debug=True)