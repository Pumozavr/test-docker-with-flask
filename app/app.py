from flask import Flask, jsonify, redirect, url_for, request
from flask.templating import render_template
from flask_restx import Api
from flask_cors import CORS
import os

secret_key = ""

def create_app():
    # Create a Flask application
    app = Flask(__name__)

    # Allow cross-origin resource sharing to let the front end access the backend
    CORS(app)

    # The flask_restx library helps us to create documentation at the /swagger-ui/ endpoint
    api = Api(app, title="Dogs API", version="0.1", doc="/swagger-ui/")


    #alternative: define a function, then later use app.add_url_rule("/","health",health) to route /health to the health function
    #@app.route("/health")
    def health():
        return jsonify("healthy")
    
    #app.view_functions['health'] = health
    app.add_url_rule('/health',"sr",health)       
    #why doesn't add_url_rule work? 
    
    @app.route("/funnyloop")
    def funnyloop():
        return render_template('Login.html')     

    #route "/" doesn't work: Not found. The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
    #@app.route("/")
    def index_not_working():
        return render_template("index.html")  
    app.add_url_rule('/','srg',index_not_working)
    
    @app.route("/index")
    def index():
        return render_template("index.html") 
    
    #give an additional argument that can be used within the corresponding function 
    @app.route("/Hasta-la-vista/<var>")
    def func(var):
        return "Hasta la vista, " + str(var)

    #redirect to another function based on a condition
    @app.route("/hello/<name>")
    def newfunc(name):
        if name.lower() == "mckinsey":
            return redirect(url_for('func', var = name))
        else: 
            return redirect(url_for('index', name = name))

    @app.route("/hello1/<name>")
    def hello1(name):
        return render_template("Hello.html", pumsa = name)


    @app.route('/success/<name>')
    def success(name):
        return 'welcome %s' % name

    @app.route('/login',methods = ['POST', 'GET'])
    def login():
        if request.method == 'POST':
            user = request.form['nm']
            return redirect(url_for('success',name = user))
        else:
            user = request.args.get('nm')
            return redirect(url_for('success',name = user))

    #app.add_url_rule('/','login',login)
    print(app.view_functions)
    return app


app = create_app()
app.run(host = "0.0.0.0", port=80)