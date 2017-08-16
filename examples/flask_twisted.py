# -*- coding: utf-8 -*-

from flask import Flask
from flask import  render_template  

#from flask.ext.twisted import Twisted
from flask_twisted import Twisted

app = Flask(__name__)

@app.route('/')  
@app.route('/<name>')  
def index(name=None):  
    print 'come into index'
    return render_template('hello.html', name=name)  

twisted = Twisted(app)


if __name__ == "__main__":
    print 'come into main'
    twisted.run(host='0.0.0.0',port=13579, debug=False) 
    #app.run(host='0.0.0.0',port=13579, debug=False) 
