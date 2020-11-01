from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def checkerboard_8 ():
    return render_template('checkbord.html')

@app.route('/<x>')
def checkerboard_4 (x):
    return render_template('checkbord_4.html', num_row=int(x))

@app.route('/<x>/<y>')
def checkerboard_x_y (x, y):
    return render_template('checkboard_x_y.html', num_row=int(x), num_column=int(y))

if __name__ =='__main__':
    app.run(debug=True) 

