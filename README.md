## Slack API Workshop

This repo contains a starting point for exploring the Slack APIs using incoming webhooks.
It's a simple app written in Python using Flask.

## What's inside
- base.html:  some bootstrap and formatting setup for flash messages
- index.html: a simple form and a navbar that links out to further Slack resources
- a server.py file with a single route to handle form submission
- a few static elements as a starting place (favicon, .css file, etc.) as well as the env requirements

## How to make it go
- `git clone` the repo from github to your desktop
- in a terminal session, open the repo and open up the file `renametosecrets.sh`
- go to api.slack.com, select Create a Custom Integration, and follow the prompts to set up an incoming webhook on your personal test team.
- copy the URL for your incoming webhook here and save it. Rename the this file `secrets.sh`
- double check that you have a .gitignore file in this repo and that `secrets.sh` is in it (so your URL will never accidentally get committed)
- back in your terminal, set up your virtual environment:
	- `source env/bin/activate`
	- `pip install -r requirements.txt`
	- `source secrets.sh`
	- `python server.py`