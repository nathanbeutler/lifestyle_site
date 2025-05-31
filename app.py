from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace this with a secure key in production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/date-ideas')
def date_ideas():
    return render_template('date_ideas.html')

@app.route('/group-hangouts')
def group_hangouts():
    return render_template('group_hangouts.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/workout', methods=['GET', 'POST'])
def workout():
    plan = None
    if request.method == 'POST':
        goal = request.form['goal']
        type = request.form['type']
        if goal == 'lose':
            plan = 'Cardio 4x/week, Light weights 3x/week'
        elif goal == 'maintain':
            plan = 'Moderate cardio 3x/week, Strength 3x/week'
        elif goal == 'gain':
            plan = 'Strength training 5x/week, Minimal cardio'
        if type == 'calisthenics':
            plan += ' using bodyweight exercises only'
    return render_template('workout.html', plan=plan)

@app.route('/budgeting')
def budgeting():
    return render_template('budgeting.html')

@app.route('/download-budget')
def download_budget():
    return send_from_directory('static', 'budget_template.xlsx', as_attachment=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

