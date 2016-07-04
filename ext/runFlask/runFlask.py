from flask import Flask,redirect,url_for
from ext.runFlask.ga import *
app = Flask(__name__)
 

app.register_blueprint(ga_IPsCount)
app.register_blueprint(ga_index)
app.register_blueprint(ga_download_check)
app.register_blueprint(ga_download_check_api)
@app.route('/')
def index():
    return '首页'
@app.route('/favicon.ico')
def fav():
    return redirect(url_for('static', filename='favicon.ico'))
    
def main():
    app.run(host='0.0.0.0', port=1995,debug=True)

