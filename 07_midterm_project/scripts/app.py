import pickle
import numpy as np
import sklearn

from flask import Flask, request, jsonify

def predict_drop(alumn, dv, model):
    X = dv.transform([alumn])
    y_pred = model.predict(X)
    return y_pred[0]


with open('xboost_model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('dropout')


@app.route('/predict', methods=['POST'])
def predict():
    alumn = request.get_json()

    prediction = predict_drop(alumn, dv, model)
    dropout = prediction >= 0.5
    
    result = {
        'dropout_probability': float(prediction),
        'dropout': bool(dropout),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)