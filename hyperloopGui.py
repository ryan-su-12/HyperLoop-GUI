from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
form_data = {'Velocity':0,'Acceleration':0,'Time': 0, 'DistanceTravelled':0, 'BatteryPercentage':0}

@app.route('/')
def home():
    
    return render_template('Home.html', variable = form_data.get('Velocity'))

@app.route('/Electrical_Subsystem/')
def Electrical_Subsystem():
    return render_template('Electrical_Subsystems.html', VelocityData = form_data.get('Velocity'), TimeData = form_data.get('Time'), AccelerationData = form_data.get('Acceleration'))

@app.route('/Mechanical_Subsystem/')
def Mechanical_Subsystem():
    return render_template('Mechanical_Subsystems.html', VelocityData = form_data.get('Velocity'), TimeData = form_data.get('Time'), AccelerationData = form_data.get('Acceleration'))

@app.route('/Input_Cases/')
def Input_Cases():
    return render_template('Input_Cases.html')

@app.route('/data/', methods = ['POST'])
def data():
    if request.method == 'POST':
        form_data['Velocity'] = request.form['Velocity']
        form_data['Time'] = request.form['Time']
        form_data['Acceleration'] = request.form['Acceleration']
        return redirect(url_for('home')), form_data

 
if __name__=='__main__':
    app.run()
