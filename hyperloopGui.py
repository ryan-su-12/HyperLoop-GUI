from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
form_data = {'Velocity':0,'Acceleration':0,'Time': 0, 'DistanceTravelled':0, 
             'BatteryPercentage':0, 'Throttle':0,
             'OutsideTemperature':0, 'Height':0, 'BatteryTemperature':100,
             'BrakePercentage':0, 'MotorTemperature':0, 'Current':0,
             'Voltage':0}

@app.route('/')
def home():
    return render_template('Home.html', VelocityData = form_data.get('Velocity'), TimeData = form_data.get('Time'), AccelerationData = form_data.get('Acceleration'), DistanceData = form_data.get('DistanceTravelled'))

@app.route('/Electrical_Subsystem/')
def Electrical_Subsystem():
    return render_template('Electrical_Subsystems.html', BatteryPercentData = form_data.get('BatteryPercentage'), CurrentData = form_data.get('Current'), VoltageData = form_data.get('Voltage'), BatteryTemperatureData = form_data.get('BatteryTemperature'))

@app.route('/Mechanical_Subsystem/')
def Mechanical_Subsystem():
    return render_template('Mechanical_Subsystems.html', ThrottleData = form_data.get('Throttle'), BrakePercentageData = form_data.get('BrakePercentage'), MotorTemperatureData = form_data.get('MotorTemperature'), HeightData = form_data.get('Height'))

@app.route('/Input_Cases/')
def Input_Cases():
    return render_template('Input_Cases.html')

@app.route('/data/', methods = ['POST'])
def data():
    if request.method == 'POST':
        form_data['Velocity'] = request.form['Velocity']
        form_data['Time'] = request.form['Time']
        form_data['Acceleration'] = request.form['Acceleration']
        form_data['DistanceTravelled'] = request.form['DistanceTravelled']
        form_data['BatteryPercentage'] = request.form['BatteryPercentage']
        form_data['Current'] = request.form['Current']
        form_data['Voltage'] = request.form['Voltage']
        form_data['BatteryTemperature'] = request.form['BatteryTemperature']
        form_data['Throttle'] = request.form['Throttle']
        form_data['Height'] = request.form['Height']
        form_data['BrakePercentage'] = request.form['BrakePercentage']
        form_data['MotorTemperature'] = request.form['MotorTemperature']
        
        return redirect(url_for('home')), form_data

if __name__=='__main__':
    app.run()