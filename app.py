import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/getstart')
def getstart():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(debug=True)