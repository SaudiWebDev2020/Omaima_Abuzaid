from flask import Flask, render_template
app= Flask(__name__)

@app.route ('/')
def hello_world():
    return render_template('index.html')

@app.route('/dojo')
def dojo ():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name (name):
    print('name')
    return 'Say'+ name +'!'

@app.route('/repeat/<no>/<word>')
def repeat (no, word):
    print('word')
    return 'say'+ word + no +'times'

if __name__ =='__main__':
    app.run(debug=True)
