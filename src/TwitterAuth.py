import os, sys
from twython import Twython

def getTwitter():

	APP_KEY = os.environ.get('APP_KEY')
	APP_SECRET = os.environ.get('APP_SECRET')
	OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
	OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')

	if APP_KEY == 'none' or APP_SECRET == 'none' or OAUTH_TOKEN == 'none' or OAUTH_TOKEN_SECRET == 'none':
		print "missing one or more Twitter authentication environment variables - terminating program"
		sys.exit

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	return twitter