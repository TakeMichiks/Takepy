from flask import jsonify
import datetime

from .. import datetime_db

@datetime_db.route("/time", methods=["GET"])
def times():
    tiempo = datetime.datetime.now()

    tiempoahora = tiempo.hour 

    tiempo_acual = tiempo.strftime("%I:%M:%p")
    if 6 <= tiempoahora < 12:
        return jsonify({"Tiempo Actual":f"{tiempo_acual}"})
    if 12 <= tiempoahora < 18:
        return jsonify({"Feliz tarde Takesito":f"{tiempo_acual}"})
    return jsonify({"Duermase Take":f"{tiempo_acual}"})
