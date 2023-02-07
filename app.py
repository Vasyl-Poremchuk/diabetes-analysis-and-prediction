import pickle
from typing import Any

import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

FEATURE_NAMES = [
    "Gender",
    "AGE",
    "Urea",
    "Cr",
    "HbA1c",
    "Chol",
    "TG",
    "HDL",
    "LDL",
    "VLDL",
    "BMI",
]


def load_model(filename: str) -> Any:
    """
    The function loads a saved prediction model.
    """
    with open(filename, "rb") as file:
        model = pickle.load(file)

    return model


@app.route("/")
def home() -> str:
    return render_template("prediction.html")


@app.route("/predict", methods=["POST"])
def predict() -> str:
    """
    The function returns the prediction result.
    """
    data = [float(feature) for feature in request.form.values()]
    x = np.array(data).reshape(1, -1)
    clf = load_model("decision_trees_model.pkl")

    input_data = pd.DataFrame(x, columns=FEATURE_NAMES)

    y_pred = clf.predict(input_data)

    return render_template(
        "prediction.html",
        prediction_text=f"Class of diabetes is {y_pred[0]} "
        "(0 - non-diabetic, 1 - pre-diabetic, 2 - diabetic)",
    )


if __name__ == "__main__":
    app.run(debug=True)
