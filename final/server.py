from flask import Flask, request, render_template, redirect, flash
from random import choice, sample
import requests
import json
import os


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)
app.secret_key = "What's up chickens what you bockin' with."

# Using Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

#######################################################################

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/submit',  methods=['POST'])
def submit_json_to_webhook():
	main_text = request.form["main-text"]
	moar_text = request.form["moar-text"]
	main_text += ("\n" + moar_text)

	title_1 = request.form["title-1"]
	text_1 = request.form["text-1"]
	color_1 = request.form["color-1"]

	title_2 = request.form["title-2"]
	text_2 = request.form["text-2"]
	color_2 = request.form["color-2"]


	title_3 = request.form["title-3"]
	text_3 = request.form["text-3"]
	color_3 = request.form["color-3"]


	#Build the JSON to send
	payload = {
		'text' : main_text,
		'attachments' : [
			{
				"color" : color_1,
				"title"	: title_1,
				"text"	: text_1,
			},
			{
				"color" : color_2,
				"title"	: title_2,
				"text"	: text_2,
			},
			{
				"color" : color_3,
				"title"	: title_3,
				"text"	: text_3,
			},
		]
	}

	url = os.environ['WEBHOOK_URL']

	print payload

	#Send it to the URL Slack provides
	r = requests.post(url, data=json.dumps(payload))
	status_code = r.status_code

	if status_code == 200:
		flash('You did it!')
		return redirect("/")
	else:
		flash('Oh no, something went wrong. You are getting a %s  status code error.' % (status_code))

	return redirect("/")



#######################################################################

if __name__ == "__main__":
    app.run(debug=True)
