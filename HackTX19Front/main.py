import webapp2
from google.appengine.api import urlfetch

class DonateHandler(webapp2.RequestHandler):
    def get(self):
        #Donate
        # self.response.write('Hello World!')
        url = 'http://www.google.com/humans.txt'

        result = urlfetch.fetch(url)
        if result.status_code == 200:
            self.response.write(result.content )
        else:
            self.response.status_code = result.status_code



app = webapp2.WSGIApplication([
    ('/merchantDonate', DonateHandler)
], debug=True)
