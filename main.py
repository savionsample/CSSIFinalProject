import webapp2
import jinja2
import os
import logging
import requests
import time

import config

from google.appengine.api import users
from google.appengine.ext import ndb

class Person(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    history = ndb.StringProperty()

class Query(ndb.Model):
    search_term = ndb.StringProperty()
    source1 = ndb.StringProperty()
    source2 = ndb.StringProperty()
    source1_name = ndb.StringProperty()
    source2_name = ndb.StringProperty()
    personKey = ndb.KeyProperty()
    time_searched = ndb.DateTimeProperty(auto_now_add=True)


def to_name(source):
    dict = {
       'abc-news' : 'ABC News',
       'associated-press' : 'Associated Press',
       'axios' : 'Axios',
       'bbc-news' : 'BBC News',
       'bloomberg' : 'Bloomberg',
       'breitbart-news' : 'Breitbart News',
       'business-insider' : 'Business Insider',
       'buzzfeed' : 'Buzzfeed',
       'cbs-news' : 'CBS News',
       'cnn' : 'CNN',
       'daily-mail' : 'Daily Mail',
       'financial-post' : 'Financial Post',
       'financial-times' : 'Financial Times',
       'fortune' : 'Fortune',
       'fox-news' : 'FOX',
       'independent' : 'Independent',
       'national-geographic' : 'National Geographic',
       'nbc-news' : 'NBC News',
       'politico' : 'Politico',
       'reuters' : 'Reuters',
       'the-american-conservative' : 'The American Conservative',
       'the-economist' : 'The Economist',
       'the-hill' : 'The Hill',
       'the-huffington-post' : 'The Huffington Post',
       'the-new-york-times' : 'The New York Times',
       'the-telegraph' : 'The Telegraph',
       'the-wall-street-journal' : 'The Wall Street Journal',
       'the-washington-post' : 'The Washington Post',
       'time' : 'Time',
       'usa-today' : 'USA Today',
       'wired' : 'Wired',
       'abc-news-au' : 'ABC News AU',
       'aftenposten' : 'Aftenposten',
       'al-jazeera-english' : 'Al Jazeera English',
       'ansa' : 'ANSA.it',
       'Argaam' : 'Argaam',
       'ars-technica' : 'Ars Technica',
       'ary-news' : 'Ary News',
       'axios' : 'Axios',
       'bild' : 'Bild',
       'blasting-news-br' : 'Blasting News Brazil',
       'business-insider-uk' : 'UK Business Insider',
       'cbc-news' : 'CBC News',
       'cnn-es' : 'CNN Spanish',
       'der-tagesspiegel' : 'Der Tagesspiegel',
       'die-zeit' : 'Die Zeit',
       'el-mundo' : 'El Mundo',
       'globo' : 'Globo',
       'goteborgs-posten' : 'Goteborgs-Posten',
       'handelsblatt' : 'Handelsblatt',
       'il-sole-24-ore' : 'Il Sole 24 Ore',
       'la-gaceta' : 'La Gaceta',
       'la-nacion' : 'La Nacion',
       'la-repubblica' : 'La Repubblica',
       'le-monde' : 'Le Monde',
       'lenta' : 'Lenta',
       'lequipe' : "L\'equipe",
       'les-echos' : 'Les Echos',
       'marca' : 'Marca',
       'svenska-dagbladet' : 'Svenska Dagbladet',
       'the-hindu' : 'The Hindu',
       'the-irish-times' : 'The Irish Times',
       'the-jerusalem-post' : 'The Jerusalem Post',
       'the-times-of-india' : 'The Times of India',
       'xinhua-net' : 'Xinhua Net',
    }
    return dict[source]

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

        template = env.get_template("templates/International.html")
        self.response.write(template.render(templateVars))
        # logging.info(response.json())

class Profile(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
            if not current_person:
                current_person = Person(email=current_email)
                current_person.put()
        else:
            self.redirect('/')
            current_person = None

        logout_url = users.create_logout_url('/')
        templateVars = {}

        try:
            # person variable
            query_query = Query.query()
            query_query = Query.query().filter(Query.personKey == current_person.key)
            query_query = query_query.order(-Query.time_searched)
            queries = query_query.fetch(limit=20) #######3

            templateVars = {
                'current_user': current_user,
                'logout_url': logout_url,
                'queries' : queries,

            }
        except AttributeError:
            self.redirect('/')


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
        search_term = self.request.get("search_term")
        source1 = self.request.get("source1")
        source2 = self.request.get("source2")
        source1_name = to_name(source1)
        source2_name = to_name(source2)
        current_user = users.get_current_user()
        people = Person.query().fetch()

        if current_user:
            current_email = current_user.email()
            current_person = Person.query().filter(Person.email == current_email).get()
            if not current_person:
                current_person = Person(email=current_email)
                current_person.put()
            source1_name = to_name(source1)
            query = Query(search_term=search_term, source1=source1, source2=source2, source1_name=source1_name,
                source2_name=source2_name, personKey=current_person.key)
            query.put()
        else:
            current_person = None

        logging.info(search_term)
        url1 = """http://newsapi.org/v2/everything?sources={source1} \
                &q={search_term} \
                &sortBy=popularity \
                &apiKey={api_key}""".format(search_term=search_term, source1=source1, api_key=config.api_key)

        url2 = """http://newsapi.org/v2/everything?sources={source2} \
                &q={search_term} \
                &sortBy=popularity \
                &apiKey={api_key}""".format(search_term=search_term, source2=source2, api_key=config.api_key)

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
             "current_person" : current_person,
             "current_user" : current_user,
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
