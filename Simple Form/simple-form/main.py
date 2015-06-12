
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome!</title>
    </head>
    <body>
        <form method="GET">
            <label>Name: </label><input type="text" name="user"/>
            <label>Email: </label><input type="text" name="email"/>
            <input type="submit" value="Submit" />
        </form>
    <body>
</html>'''
        print self.request.GET['user']
        self.response.write(page) #PRINT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
