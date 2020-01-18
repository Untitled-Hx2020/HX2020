from flask import Flask
from flaskwebgui import FlaskUI   # get the FlaskUI class


app = Flask(__name__)
ui = FlaskUI(app)                 # feed the parameters


# do your logic as usual in Flask

@app.route("/")
def index():
    return '''

<html>
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>'''
ui.run()
