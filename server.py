"""Greeting Flask app."""

from random import choice

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

    return "<!doctype html><html><a href='http://localhost:5000/hello'>Hi! This is the home page.</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliment_choices = "<select name='compliments'>"

    for compliment in AWESOMENESS:
        compliment_choices = compliment_choices + "<option value='{}'>{}</option>".format(compliment, compliment)
    compliment_choices = compliment_choices + "</select>"

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          {}<br><input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(compliment_choices)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliments")
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
