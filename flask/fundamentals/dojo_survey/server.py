from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ["POST"])
def result():
    print("Submitted Info")
    print(request.form)
    name_from_form = request.form["name"]
    location_from_form = request.form["location"]
    language_from_form = request.form["language"]
    comment_from_form = request.form["comment"]
    return render_template('result.html', temp_name = name_from_form, temp_location = location_from_form, temp_lang = language_from_form, temp_comment = comment_from_form)

if __name__ == "__main__":
    app.run(debug = True)
