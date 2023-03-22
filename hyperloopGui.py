
from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Battery/')
def Battery():
    return render_template('Battery.html')

@app.route('/Velocity/')
def Velocity():
    return render_template('Velocity.html')

@app.route('/Temperatures/')
def Temperatures():
    return render_template('Temperatures.html')

@app.route('/System_Status/')
def System_Status():
    return render_template('System_Status.html')


if __name__=='__main__':
    app.run()