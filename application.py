from flask import Flask
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
        viewdrop=''
        for il in l:
            if (il!='' and il[0]=='#'):
                istring="<li class='disable'>{}</li>".format(il)
            else:
                istring="<li class='able'>{}</li>".format(il)
            viewdrop +=istring
        return render_template('index.html',viewdropsetting=viewdrop)
    return app