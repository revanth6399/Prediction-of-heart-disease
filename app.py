import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('temp.pkl','rb'))

@app.route('/')
def home():
    values = request.values
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    
    return render_template('predict.html', prediction_text = 'The chances of heart disease is $ {}'. format(output))


if __name__ == "__main__":
    app.run(debug=True)

    
    
     