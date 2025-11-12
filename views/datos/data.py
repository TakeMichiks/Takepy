import json
from .. import datos_db
from flask import jsonify, request
from marshmallow import ValidationError
from pathlib import Path
from ..serializer import libro_schema, libros_schema,DataTeachersSchema
import os

@datos_db.route("/hello", methods=["GET"])
def hello():
    return jsonify({"hello": "Arrosx"})


DB_FILE = "libros.json"


def leer_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def escribir_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# --- Rutas de la API de Libros ---
@datos_db.route("/libros", methods=["GET", "POST"])
def manejar_libros():
    if request.method == "POST":
        json_data = request.get_json()
        if not json_data:
            return jsonify({"error": "No se recibieron datos"}), 400

        try:
            datos_libro = libro_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422

        libros = leer_db()
        nuevo_id = libros[-1]["id"] + 1 if libros else 1
        datos_libro["id"] = nuevo_id

        libros.append(datos_libro)
        escribir_db(libros)

        return libro_schema.jsonify(datos_libro), 201

    if request.method == "GET":
        libros = leer_db()
        return libros_schema.jsonify(libros)

BASE_DIR = Path(__file__).parent / "data" / "dataTeaches.json"

def teachersview():
    try:
        BASE_DIR.parent.mkdir(parents=True, exist_ok=True)

        with open(BASE_DIR, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def teacherssave(data):
    with open(BASE_DIR, "w") as f:
        json.dump(data, f, indent=2)
    



@datos_db.route("/Teachers", methods=["POST"])
def teachers():
    
    data_techers = request.get_json()

    if not data_techers:
        return jsonify({"Error":"Data is invalid or don`t leave blank"}),401

    try:
        dataverify = DataTeachersSchema().load(data_techers)
    except ValidationError as err:
        return jsonify({"Error":f"Validation Error verific data {err}"}),402
     
    datateachersview = teachersview()
    new_id = datateachersview[-1]["id"] + 1 if datateachersview else 1
    dataverify["id"] = new_id

    datateachersview.append(dataverify)
    teacherssave(datateachersview)

    return jsonify({"success":f"data is save{BASE_DIR}"})





