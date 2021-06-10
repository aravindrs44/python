from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x = 3)

@app.route('/play/<int:x>')
def playbox(x):
    return render_template('index.html', x = x)

@app.route('/play/<int:x>/<colors>')
def colorbox(x, colors):
    return render_template('index.html', x = x, colors = colors)

if __name__=="__main__":
    app.run(debug = True)