# IMPORTS
from flask import jsonify, request
from marshmallow import ValidationError
from pathlib import Path
from tinydb import TinyDB

# import Serializer
from ..serializer import DataTeachersSchema, DataStudentsSchema

# import rute
from .. import datos_db

# Archivos Json
db = TinyDB("Students_database.json", indent=4)
dbteachers = TinyDB("Teachers_database.json", indent=4)

# Tablas
students_table = db.table("Students")
teacher_table = dbteachers.table("Teachers")

# DIRS
TEACHERS_DIR = Path(__file__).parent / "data" / "dataTeaches.json"
STUDENTS_DIR = Path(__file__).parent / "data" / "dataStudents.json"

## START DEF ROUTES

## ROUTE TEST LIVE FILE
@datos_db.route("/hello", methods=["GET"])
def hello():
    return jsonify({"hello": "is alive route"})


# TEACHERS
@datos_db.route("/TeachersData", methods=["GET"])
def teachersdata():
    all_teachers = teacher_table.all()

    for teachers in all_teachers:
        teachers["id"] = teachers.doc_id
    return jsonify(all_teachers)


@datos_db.route("/Teachers", methods=["POST"])
def teachers():
    data_techers = request.get_json()

    if not data_techers:
        return jsonify({"Error": "Data is invalid or don`t leave blank"}), 401

    try:
        dataverify = DataTeachersSchema().load(data_techers)
    except ValidationError as err:
        return jsonify({"Error": f"Validation Error verific data {err}"}), 402

    # Mejora del codigo
    teachers_id = teacher_table.insert(dataverify)

    return jsonify({"success": f"data is save{teachers_id}"}), 200


# STUDENTS

@datos_db.route("/StudentsData", methods=["GET"])
def studentsdata():
    all_students = students_table.all()

    for students in all_students:
        students["id"] = students.doc_id
    return jsonify(all_students)


@datos_db.route("/Students", methods=["POST"])
def students():
    data_students = request.get_json()

    if not data_students:
        return jsonify({"Error": "los datos estan vacios"}), 401

    try:
        dataverify = DataStudentsSchema().load(data_students)
    except ValidationError as err:
        return jsonify({"Error": f"data is not valid,verific data:{err}"})

    students_id = students_table.insert(dataverify)

    return jsonify({"success": f"data is save{students_id}"}), 200
