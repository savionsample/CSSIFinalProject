import webapp2
import jinja2
import os
import logging
import requests
import time

from google.appengine.api import users
from google.appengine.ext import ndb


# print('NEWSAPIDIRECTORY', dir(newsapi))
# newsapi = NewsApiClient(api_key='334b68e424df4756b9a3bbb3caba75bd')

class Person(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()

class Query(ndb.Model):
    search_term = ndb.StringProperty()
    source1 = ndb.StringProperty()
    source2 = ndb.StringProperty()
        
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):

        search_term = self.request.get("search_term")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")

        #login
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
            # Putting term into url
            "search_term" : search_term,
            "source1" : source1,
            "source2": source2
        }
        print(source1)
        template = env.get_template("templates/home.html")
        self.response.write(template.render(templateVars))
        # logging.info(response.json())

class USInternational(webapp2.RequestHandler):
    def get(self):

        search_term = self.request.get("search_term")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")

        #login
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
            # Putting term into url
            "search_term" : search_term,
            "source1" : source1,
            "source2": source2
        }
        print(source1)
        template = env.get_template("templates/USInternational.html")
        self.response.write(template.render(templateVars))
        # logging.info(response.json())

class International(webapp2.RequestHandler):
    def get(self):

        search_term = self.request.get("search_term")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")

        #login
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
            # Putting term into url
            "search_term" : search_term,
            "source1" : source1,
            "source2": source2
        }
        print(source1)
        template = env.get_template("templates/International.html")
        self.response.write(template.render(templateVars))
        # logging.info(response.json())


class Profile(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email() #?
        else:
            current_person = None
        logout_url = users.create_logout_url('/')
        templateVars = {
            'current_user': current_user,
            'logout_url': logout_url,
        }
        template = env.get_template('templates/profile.html')
        self.response.write(template.render(templateVars))

class CreateAccount(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        current_user = users.get_current_user()
        email = current_user.email()
        person = Person(name=name, email=email)
        person.put()
        time.sleep(2) #to fix the delay refresh
        self.redirect('/')

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
        response2 = requests.get(url2)
        json1 = response1.json()
        json2 = response2.json()

        articles1 = json1["articles"]
        articles2 = json2["articles"]
        templateVars = {
             "search_term" : search_term,
             "source1" : source1,
             "source2": source2,
             "articles1" : articles1,
             "articles2" : articles2,
        }

        template = env.get_template('templates/results.html')
        self.response.write(template.render(templateVars))



class About(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email() #?
        else:
            current_person = None
        logout_url = users.create_logout_url('/')
        templateVars = {
            'current_user': current_user,
            'logout_url': logout_url,
        }
        template = env.get_template("templates/about.html")
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the MainPage Handler
    ('/profile', Profile),
    ('/create', CreateAccount),
    ('/results', ResultsPage),
    ('/usinternational', USInternational),
    ('/international', International),
    ('/about', About),



], debug=True)
