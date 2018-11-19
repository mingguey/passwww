from flask import Flask, request
from flask import render_template

def creat_app(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
        
    @app.route('/')
    def index():
        dropf='dropdomain.txt'
        f=open(dropf)
        l=(f.read()).split('\n')
        dropset=""
        for i in range(len(l)):
            dropset +=l[i]
            dropset +='\n'
        return render_template('index.html',ils=l,vs=dropset)
    
    @app.route('/edit', methods=['POST'])
    def edit():
        dropset= request.form['dropset']
        l=[]
        return  render_template('index.html',ils=l,vs=dropset)
    
    return app

