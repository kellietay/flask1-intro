"""Greeting Flask app."""

from random import choice, randint

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    	<br><br><a href="/hello">hello</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    y = randint(0,1)
    if y == 0:
    	output = "/greet"
    else:
    	output = "/diss"
    html = open("demo.html")
    html_text = html.read()
    html.close()
    return html_text.format(output)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>Diss</title>
      </head>
      <body>
        Hi, {}! I think you're as {} as a pig !
      </body>
    </html>
    """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
