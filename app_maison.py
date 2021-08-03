# import a library

from flask import Flask, render_template, request
import joblib

# instance of an app
app = Flask(__name__)

lm = joblib.load('maison.pkl')

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/end', methods= ['POST'])
def result():
    a = request.form.get('area')
    b = request.form.get('rooms')
    c = request.form.get('bathroom')
    d = request.form.get('floors')
    e = request.form.get('driveway')
    f = request.form.get('game_room')
    g = request.form.get('cellar')
    h = request.form.get('gas')
    i = request.form.get('air')
    j = request.form.get('garage')
    k = request.form.get('situation')
   

    pred = lm.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i),int(j),int(k)]])
    print(pred)
    return render_template('result.html', predicted_text = f'The estimated price is {pred} INR')
    


# run the app
if __name__ == '__main__':
    app.run(debug= True)