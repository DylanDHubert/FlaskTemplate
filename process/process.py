from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

filepath = "images"



@app.route('/')
def function():
    print("TEST")
    return jsonify({'message': "TEST"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
