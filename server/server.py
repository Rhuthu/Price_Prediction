from flask import Flask, request, jsonify,send_from_directory
import util
import os


# Absolute path to client folder
CLIENT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'client'))

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(CLIENT_FOLDER, 'app.html')

@app.route('/client/<path:filename>')
def serve_static(filename):
    return send_from_directory(CLIENT_FOLDER, filename)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()