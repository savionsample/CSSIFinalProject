import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/home.html')
        self.response.write(template.render())

class Results(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/results.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", HomePage),
    ("/results", Results)
], debug = True)
