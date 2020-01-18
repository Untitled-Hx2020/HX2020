from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI   # get the FlaskUI class


app = Flask(__name__)
ui = FlaskUI(app)                 # feed the parameters


# do your logic as usual in Flask

#@app.route("/")
#def index():
#    return '''     '''

@app.route('/')
def index():
    your_list= [1,2,3,4]
    return render_template('your_view.html', your_list=your_list)

ui.run()
