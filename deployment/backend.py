from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

columns = ["AT", "AP", "AH", "AFDP", "GTEP", "TIT", "TAT", "TEY", "CDP"]
with open("rf_pipe.pkl", "rb") as f:
    model_rf = pickle.load(f)

@app.route("/")
def homepage():
    return "<h1>Backend Pemodelan Emisi CO dan NOx </h1>"

@app.route("/emisi", methods=["GET", "POST"])
def emisi():
    if request.method == 'POST':
        data = request.json
        new_data = [data["AT"], 
                    data["AP"],
                    data["AH"],
                    data["AFDP"],
                    data["GTEP"],
                    data["TIT"],
                    data["TAT"], 
                    data["TEY"], 
                    data["CDP"]]
        new_data = pd.DataFrame([new_data], columns=columns)
        res = model_rf.predict(new_data)
        response = {"code":200, "status":"OK",
                    "result": res[0].tolist()}
        return jsonify(response)
    return "Silakan gunakan method post untuk mengakses model random forest regressor"

app.run(debug=True)