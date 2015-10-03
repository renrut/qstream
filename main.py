import webapp2
import jinja2
import os

from google.appengine.ext import db
from google.appengine.api import users



template_dir = os.path.dirname(__file__)
template_dir = template_dir
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


class musicQueue(db.Model):
	user = db.StringProperty(required=True)
	queue = db.PickleProperty(required=True)


class MainHandler(webapp2.RequestHandler):
	
	def render_front(self, error=""):
		template = jinja_env.get_template("front.html")
		self.response.out.write(template.render())
	def get(self):
		self.render_front()



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
