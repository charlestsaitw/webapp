from flask import Flask, render_template, jsonify, send_from_directory
from sqlite3 import connect
app = Flask(__name__, template_folder='../dist')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html')

# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('../dist', path)

@app.route('/app_bundle.js')
def send_js():
    return send_from_directory('../dist', 'app_bundle.js')

@app.route("/list")
def list():
    db = connect('test.db')
    output = []
    c = db.execute('select name, long_descript from items')
    for row in c:
        output.append({'name': row[0], 'url': row[1]})
    return jsonify(output)
