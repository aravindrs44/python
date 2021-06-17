
from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'find out on the next episode of dragonball z'

@app.route('/')
def index():
    if 'visits' in session:
        print('visits exists!')
        session['visits'] += 1
    else:
        print("key does NOT exist")
        session['visits'] = 0
    print(session['visits'])
    return render_template('index.html')

@app.route('/destroy_session')
def erase():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)