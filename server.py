from flask import Flask
app = Flask(__name__)

#code to load model

@app.route('/score')
def score():
    return 'Hello, World!'

@app.route('/test')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()