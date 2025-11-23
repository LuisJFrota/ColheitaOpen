from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def listValues():
    return "list"

app.run(port=5000, host='localhost', debug=True)