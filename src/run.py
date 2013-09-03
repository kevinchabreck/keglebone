import sys, os
import TwitterAuth
from twython import Twython

twitter = TwitterAuth.getTwitter()

twitter.update_status(status='test')
#print "starting script"
