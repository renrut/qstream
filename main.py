import webapp2
#import spotipy
#import soundcloud
import jinja2
import os
from google.appengine.ext import db
from google.appengine.api import users


template_dir = os.path.dirname(__file__)
template_dir += "/partials"
print template_dir
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


SOUNDCLOUD_CLIENT_ID = "354f852cc7ba9c95b38ef4e21abd520b"
SOUNDCLOUD_CLIENT_SECRET = "b69dceca1b9ee7138eef75d5de3607a5"
#export SPOTIPY_CLIENT_ID='627c0a1371a04a46abcbe5cbd3ff6d8a'
#export SPOTIPY_CLIENT_SECRET='fdaa139f485b44ff93b98154261e4bd9'
#export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

#token = util.prompt_for_user_token(username, scope)


class MainHandler(webapp2.RequestHandler):
	
	def render_front(self, error=""):
		template = jinja_env.get_template("front.html")
		self.response.out.write(template.render())
	
	def render_login(self, error=""):
		template = jinja_env.get_template("login.html")
		self.response.out.write(template.render())
	def get(self):
		self.render_login()
	
	# def get(self):
	# 	if users.get_current_user():
	# 		self.render_front()
	# 	else:
	# 		render_login()






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
