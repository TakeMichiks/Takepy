import json
from .. import datos_db
from flask import jsonify, request
from marshmallow import ValidationError
from pathlib import Path
from ..serializer import DataTeachersSchema

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
#---------------------------

# DEF STUDENDS ------------
def studentview():
    try:
        STUDENTS_DIR.parent.mkdir(parents=True,exist_ok=True)

        with open(studentview, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            return []


def sturdentsave(data):
    with open(STUDENTS_DIR, "w") as f:
        json.dump(data, f, indent=2)
#--------------------------

## ROUTE TEST LIVE FILE
@datos_db.route("/hello", methods=["GET"])
def hello():
    return jsonify({"hello": "Arrosx"})

## START DEF ROUTES
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

    return jsonify({"success":f"data is save{TEACHERS_DIR}"})





