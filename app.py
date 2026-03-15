from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load models
maison_model = joblib.load("models/maison_random_forest_model.pkl")
appart_model = joblib.load("models/apt_random_forest_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    form_type = None

    if request.method == "POST":

        form_type = request.form.get("form_type")

        longitude = float(request.form["longitude"])
        latitude = float(request.form["latitude"])
        code_postal = float(request.form["code_postal"])
        surface_reelle_bati = float(request.form["surface_reelle_bati"])
        nombre_pieces_principales = float(request.form["nombre_pieces_principales"])
        prix_m2_ref = float(request.form["prix_m2_ref"])
        number_of_lots = float(request.form["number_of_lots"])

        if form_type == "maison":

            surface_terrain = float(request.form["surface_terrain"])

            features = np.array([[

                longitude,
                latitude,
                code_postal,
                surface_reelle_bati,
                nombre_pieces_principales,
                prix_m2_ref,
                surface_terrain,
                number_of_lots

            ]])

            prediction = maison_model.predict(features)[0]


        elif form_type == "appartement":

            total_carrez_surface = float(request.form["total_carrez_surface"])

            features = np.array([[

                longitude,
                latitude,
                code_postal,
                surface_reelle_bati,
                nombre_pieces_principales,
                prix_m2_ref,
                total_carrez_surface,
                number_of_lots

            ]])

            prediction = appart_model.predict(features)[0]

    return render_template("index.html", prediction=prediction, form_type=form_type)


if __name__ == "__main__":
    app.run(debug=True)