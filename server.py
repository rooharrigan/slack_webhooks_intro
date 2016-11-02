from flask import Flask, request, render_template, redirect, flash
from random import choice, sample
import requests
import json
import os

app = Flask(__name__)
app.secret_key = "SHHHHH ITS A SECRETTTTT."

# We will use os.environ to get at the secret URL as an environmental variable
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

#######################################################################

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/submit',  methods=['POST'])
def submit_json_to_webhook():
	main_text = request.form["**"]
	# moar_text = grab the information coming from your form element named 'moar-text'
	# main_text += ("\n" + moar_text)

	# Same as above, grab the info coming from your title, text, and color form elements.
	# and put fill in the skeleton of the attachemnts dictionary below.
	# title_1 =
	# text_1 =
	# color_1 = editing for testing purpose


	#Build the JSON to send
	payload = {
		'text' : main_text,
		# 'attachments' : [
		# 	{
				# "color" :
		# 	},
		# ]
	}

	# Your secret URL sourced in from secrets.sh
	url = os.environ['WEBHOOK_URL']

	# Send a JSONified version of your payload to the URL Slack provides
	r = requests.post(url, data=json.dumps(payload))
	status_code = r.status_code

	# Check the status code of the respond you receive from Slack.
	# If it's an error, flash a message about it at the bottom of the page.
	if status_code == 200:
		flash('You did it!')
		return redirect("/")
	else:
		flash('Oh no, something went wrong. You are getting a %s  status code error.' % (status_code))

	return redirect("/")



#######################################################################

if __name__ == "__main__":
    app.run(debug=True)
