from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Word!'

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hi(name):
    return "Hi " + name
    
@app.route('/say/flask')
def hiF():
    return "Hi Flask!"

@app.route('/say/michael')
def hiM():
    return "Hi Michael!"

@app.route('/say/john')
def hiJ():
    return "Hi John!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return int(num) * word

if __name__=="__main__":
    app.run(debug=True)