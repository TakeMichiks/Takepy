# IMPORTS
import json
from flask import jsonify, request
from marshmallow import ValidationError
from pathlib import Path

# import Serializer
from ..serializer import DataTeachersSchema, DataStudentsSchema

# import rute
from .. import datos_db

# DIRS
TEACHERS_DIR = Path(__file__).parent / "data" / "dataTeaches.json"
STUDENTS_DIR = Path(__file__).parent / "data" / "dataStudents.json"

## DEF PRINCIPAL FOR READ AND SAVE DATA


# DEF TEACHERS -----------
def teachersview():
    try:
        TEACHERS_DIR.parent.mkdir(parents=True, exist_ok=True)

        with open(TEACHERS_DIR, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def teacherssave(data):
    with open(TEACHERS_DIR, "w") as f:
        json.dump(data, f, indent=2)


# ---------------------------


# DEF STUDENDS ------------
def studentview():
    try:
        STUDENTS_DIR.parent.mkdir(parents=True, exist_ok=True)

        with open(studentview, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sturdentsave(data):
    with open(STUDENTS_DIR, "w") as f:
        json.dump(data, f, indent=2)


# --------------------------

## START DEF ROUTES


## ROUTE TEST LIVE FILE
@datos_db.route("/hello", methods=["GET"])
def hello():
    return jsonify({"hello": "is alive route"})


# TEACHERS
@datos_db.route("/TeachersData", methods=["GET"])
def teachersdata():
    data = teachersview()
    return jsonify(data)


@datos_db.route("/Teachers", methods=["POST"])
def teachers():
    data_techers = request.get_json()

    if not data_techers:
        return jsonify({"Error": "Data is invalid or don`t leave blank"}), 401

    try:
        dataverify = DataTeachersSchema().load(data_techers)
    except ValidationError as err:
        return jsonify({"Error": f"Validation Error verific data {err}"}), 402

    datateachersview = teachersview()
    new_id = datateachersview[-1]["id"] + 1 if datateachersview else 1
    dataverify["id"] = new_id

    datateachersview.append(dataverify)
    teacherssave(datateachersview)

    return jsonify({"success": f"data is save{TEACHERS_DIR}"}), 200


# STUDENTS


@datos_db.route("/StudentsData", methods=["GET"])
def studentsdata():
    data = studentview()
    return jsonify(data)


@datos_db.route("/Students", methods=["POST"])
def students():
    data_students = request.get_json()

    if not data_students:
        return jsonify({"Error": "los datos estan vacios"}), 401

    try:
        dataverify = DataStudentsSchema().load(data_students)
    except ValidationError as err:
        return jsonify({"Error": f"data is not valid,verific data:{err}"})

    datastudentsview = studentview()
    new_id = datastudentsview[-1]["id"] + 1 if datastudentsview else 1
    dataverify["id"] = new_id

    datastudentsview.append(dataverify)
    sturdentsave(datastudentsview)

    return jsonify({"success": f"data is save{STUDENTS_DIR}"}), 200
