from flask import Flask, render_template
app= Flask (__name__)

@app.route('/play')
def blue_boxes ():
    return render_template('blue.html')

@app.route('/play/<x>')
def blue_boxes_x (x):
    return render_template('blue_x.html', num_times=int(x))

@app.route('/play/<x>/<string:color>')
def boxes_color (x, color):
    return render_template('x_color.html', num_times=int(x), some_color= color)

if __name__ =='__main__':
    app.run(debug=True) 

