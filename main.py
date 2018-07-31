import webapp2
import jinja2
import os
import logging
import requests

from google.appengine.api import users
from google.appengine.ext import ndb


# print('NEWSAPIDIRECTORY', dir(newsapi))

 # newsapi = NewsApiClient(api_key='334b68e424df4756b9a3bbb3caba75bd')

# let query =`${url}?api_key=${apiKey}&q=${searchTerm}&limit=1`;

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):


        template = env.get_template('templates/home.html')
        self.response.write(template.render())
        # logging.info(response.json())
        #login
        # current_user = users.get_current_user()
        # people = Person.query().fetch()
        # if current_user:
        #     current_email = current_user.email() #?
        #     current_person = Person.query().filter(Person.email == current_email).get()
        # else:
        #     current_person = None
        # logout_url = users.create_logout_url('/')
        # login_url = users.create_login_url('/')
        # templateVars = {
        #     'current_user': current_user,
        #     'login_url': login_url,
        #     'logout_url': logout_url,
        #     'current_person': current_person,
        # }
        # template = env.get_template('templates/home.html')
        # self.response.write(template.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        search_term = self.request.get("search_term")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")
        # template = env.get_template("templates/home.html")
        templateVars = {
            "search_term" : search_term,
            "source1" : source1,
            "source2": source2
        }

        url = 'http://newsapi.org/v2/top-headlines?q=' + search_term + '&apiKey=334b68e424df4756b9a3bbb3caba75bd'

        print('URLLLLLLLLLLLLLL' + url)
        response = requests.get(url)
        print(response.json())

        template = env.get_template('templates/results.html')
        self.response.write(template.render(templateVars))





app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the MainPage Handler
    ('/results', ResultsPage),
], debug=True)
