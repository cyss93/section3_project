import pickle
from flask import Flask, render_template, request

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['GET','POST'])
def tmp():
    symboling = int(request.form['symboling'])
    wheelbase = float(request.form['wheelbase'])
    carlength = float(request.form['carlength'])
    carwidth = float(request.form['carwidth'])
    carheight = float(request.form['carheight'])
    curbweight = int(request.form['curbweight'])
    enginesize = int(request.form['enginesize'])
    boreratio = float(request.form['boreratio'])
    stroke = float(request.form['stroke'])
    compressionratio = float(request.form['compressionratio'])
    horsepower = int(request.form['horsepower'])
    peakrpm = int(request.form['peakrpm'])
    citympg = int(request.form['citympg'])
    highwaympg = int(request.form['highwaympg'])

    X_1 = [symboling, wheelbase, carlength, carwidth, carheight, curbweight, enginesize, 
    boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]
    value = model.predict([X_1])

    # value = symboling + wheelbase + carlength + carwidth + carheight + curbweight + enginesize + boreratio + stroke + compressionratio + horsepower + peakrpm + citympg + highwaympg
    return render_template('post.html', value = value)

if __name__ == '__main__':
    app.run(debug=True)