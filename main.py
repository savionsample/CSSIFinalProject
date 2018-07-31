import webapp2
import jinja2
import os
import logging
import requests

from google.appengine.api import users
from google.appengine.ext import ndb

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

        logging.info(search_term)
        url1 = """http://newsapi.org/v2/everything?sources={source1} \
                &q={search_term} \
                &sortBy=popularity \
                &apiKey=334b68e424df4756b9a3bbb3caba75bd""".format(search_term=search_term, source1=source1)

        url2 = """http://newsapi.org/v2/everything?sources={source2} \
                &q={search_term} \
                &sortBy=popularity \
                &apiKey=334b68e424df4756b9a3bbb3caba75bd""".format(search_term=search_term, source2=source2)


        response1 = requests.get(url1)
        json1 = response1.json()
        response2 = requests.get(url2)
        json2 = response2.json()
        print('json1:'+ str(json1))
        print('json2: '+ str(json2 ))
        articles1 = json1["articles"]
        articles2 = json2["articles"]
        print("source are: ")
        print(source1)
        print(source2)
        templateVars = {
             "search_term" : search_term,
             "source1" : source1,
             "source2": source2,
             "articles1" : articles1,
             "articles2" : articles2,

        }




        # print(articles[0]["title"])
        # print(response.json())

        template = env.get_template('templates/results.html')
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the MainPage Handler
    ('/results', ResultsPage),
], debug=True)
