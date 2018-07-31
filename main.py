import webapp2
import jinja2
import os
import logging
import requests

from google.appengine.api import users
from google.appengine.ext import ndb


# print('NEWSAPIDIRECTORY', dir(newsapi))

 # newsapi = NewsApiClient(api_key='334b68e424df4756b9a3bbb3caba75bd')

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):

        searchTerm = self.request.get("searchTerm")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")
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
        template = env.get_template("templates/home.html")
        templateVars = {
            "searchTerm" : searchTerm,
            "source1" : source1,
            "source2": source2
        }
        print(source1)
        self.response.write(template.render(templateVars))
        # logging.info(response.json())

class ResultsPage(webapp2.RequestHandler):
    def get(self):

        url = ('http://newsapi.org/v2/top-headlines?'
                'source={{source1}}}&'
                'q={{searchTerm}}&'
                'apiKey=334b68e424df4756b9a3bbb3caba75bd')
        response = requests.get(url)
        print(response.json())

        template = env.get_template('templates/results.html')
        self.response.write(template.render())

    def post(self):
        pass
        # q = self.request.get('q')
        #
        # url = ('http://newsapi.org/v2/top-headlines?'
        #         'q=' + q + 'apiKey=334b68e424df4756b9a3bbb3caba75bd')
        # response = requests.get(url)
        # print(response.json())





app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the MainPage Handler
    ('/results', ResultsPage),
], debug=True)
