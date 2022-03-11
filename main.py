from flask import Flask, render_template,url_for,redirect
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    # return render_template('index.html')
    colors=['Red','Blue','Yellow']
    return render_template('index.html',colors=colors)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/css')
def css():
    return render_template('css.html')
@app.route('/dog')
def dog():
    return render_template('dog.html')
@app.route('/fox')
def fox():
    return render_template('fox.html')
@app.route('/croc')
def croc():
    return render_template('croc.html')
if __name__ == '__main__':
    app.run(debug= True)
