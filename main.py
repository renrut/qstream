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



class userDB(db.Model):
	userID=db.StringProperty(required=True)
	spotifytoken = db.StringProperty(required=True)
	soundcloudtoken = db.StringProperty(required=True)



class MainHandler(webapp2.RequestHandler):
	
	def render_front(self, error=""):
		template = jinja_env.get_template("front.html")
		self.response.out.write(template.render())
	
	def render_googleLogin(self, error=""):
		greeting = ('<a href="%s">Sign in or register</a>.' %
                      users.create_login_url('/'))
		self.response.out.write(greeting)

	def render_login(self, error=""):
		template = jinja_env.get_template("login.html")
		self.response.out.write(template.render())
	

	def get(self):
		#getting current user
		user = users.get_current_user()
		
		
		#if user doesnt exist
		if not user:
			self.render_googleLogin()

		else:
			#querying gql db for user tokens for api
			#userTok = db.GqlQuery("SELECT * FROM userDB")
       	 	#myUser = userTok.get_by_id(int(post_id)) 
			
			#checking to see if user has tokens
			#if spotifytoken == "" or soundcloudtoken == "":
			#	self.render_login()
			#else:
				self.render_front()
	





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
