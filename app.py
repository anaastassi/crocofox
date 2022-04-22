
from flask import Flask, render_template,url_for,redirect

from flask_bootstrap import Bootstrap
from flask import request

# from db import get,set,init

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
@app.route('/myfox')
def myfox():
    return render_template('myfox.html')
@app.route('/name')
def name():
    myname = request.args.get('usertext')
    print(myname)
   
    return render_template('name.html', myname = myname)
    # return '''<h1>Now you have your fox {}</h1>'''.format(myname)
@app.route('/crocuk')
def crocuk():
    return render_template('crocuk.html')











if __name__ == '__main__':
    # db=init()
    #
    # # set(db,'2',data)
    # print("данные из базы:"+str(get(db,"lovely")[1]))

    app.run(debug= True)
