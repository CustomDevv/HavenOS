from flask import Flask, render_template, request, session, redirect, url_for
import psutil

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login validation logic here
        # For simplicity, let's assume valid credentials
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    return render_template('dashboard.html', cpu_percent=cpu_percent, ram_percent=ram_percent)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
