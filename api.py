from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import numpy as np
import pickle
import json
import os

import tensorflow as tf

app = Flask(__name__)
api = Api(app)


# Parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='name in arabic')


# Recieving data through post request
class NameIdentifier(Resource):
    def post(self):
        args = parser.parse_args()
        name_str = args['name']
        # adding start and end tokens
        name_str = '<sos> ' + name_str + ' <eos>'
        # tokenize our name
        name_toks = tokenizer.texts_to_sequences([name_str])
        # make prediction
        prediction = tf.nn.sigmoid(model.predict(name_toks)).numpy()
        
        # threshold
        correct = False
        if prediction[0][0] > .80:
            correct = True

        result = {
            "name recieved": name_str,
            "name tokens": name_toks,
            "prediction": f"{prediction[0][0]:.3f}",
            "is it a correct name": correct
        }
        return jsonify(result)


api.add_resource(NameIdentifier, '/name')

if __name__ == '__main__':
    # Load tokenizer
    with open("models/realdata_40k_lstm_over_engineered.pickle", 'rb') as f:
        tokenizer = pickle.load(f)

    # Load model
    model = tf.keras.models.load_model('models/realdata_40k_lstm_over_engineered.h5')
    print(model.summary())
    print("Model used: realdata_40k_lstm_over_engineered.h5")
    # Run the app in DEBUG MODE
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)