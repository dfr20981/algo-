from flask import app, render_template
import flask

app = flask(__name__)



@app.route('/log')
def log():
    return render_template('log/log.html')



def ini_app(config):
    app.config.from_object(config)
 
    return app
