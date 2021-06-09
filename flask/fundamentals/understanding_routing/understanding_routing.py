from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/<name>')
def statename(name):
    return f"Hello {name}"

@app.route('/repeat/<reps>/<word>')
def repeatword(reps, word):
    reps = int(reps)
    return word * reps

if __name__=="__main__":
    app.run(debug=True)