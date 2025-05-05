from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to something unique

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement your login logic here
        username = request.form['username']
        password = request.form['password']
        if username == 'your_username' and password == 'your_password':
            session['logged_in'] = True
            return redirect(url_for('gallery'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/gallery')
def gallery():
    if 'logged_in' in session:
        folder = os.path.join('static/uploads')
        photos = os.listdir(folder)
        photos = ['uploads/' + photo for photo in photos]
        return render_template('gallery.html', photos=photos)
    return redirect(url_for('login'))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
