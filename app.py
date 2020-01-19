from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


f= open("list_doc","r+")
list = f.read().splitlines()

f2 = open("success_doc", "r")
succ_list = f2.read().splitlines()

@app.route('/')
def index():
    return render_template('index.html', list = list)

@app.route('/profile.html')
def profile():
    return render_template('profile.html', succ_list = succ_list)

@app.route('/new.html')
def new():
    return render_template('new.html')



app.run()