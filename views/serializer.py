from marshmallow import fields, validate
from . import ma


class DataTeachersSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Str(required=True)
    phone = fields.Int(required=True)
    direction = fields.Str(required=True)
    yearasigned = fields.Str(required=True)
    titledoc = fields.Str(required=True)
    disability = fields.Str(allow_none=True)

    class Meta:
        fields = (
            "id",
            "name",
            "age",
            "phone",
            "direction",
            "yearasigned",
            "titledoc",
            "disability",
        )


class DataStudentsSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True, error_messages={"required": "Requiered Name Student"}
    )
    age = fields.Str(
        required=True, error_messages={"required": "Requiered Age the Student"}
    )
    yearstudent = fields.Str(
        required=True,
        error_messages={"required": "Requiered year Student verific data"},
    )
    dni = fields.Str(
        allow_none=True,
        validate=validate.Length(
            min=2,
            max=12,
            error="Error no puede tener menos de 4 digitos y mayor de 12 digitos verifique",
        ),
    )
    family = fields.Str(
        required=True, error_messages={"required": "Required Name Family"}
    )
    phone = fields.Int(
        required=True,
        error_messages={"required": "Required Phone Father/Mother or Family"},
    )
    note = fields.Str(allow_none=True)

    class Meta:
        fields = ("id", "name", "age", "yearstudent", "dni", "family", "phone", "note")


# --- Instancias del Schema para uso en las rutas ---
# Se exportan para poder importarlas directamente en los archivos de rutas.
dataTeachers_schema = DataTeachersSchema(many=True)
dataStudents_Schema = DataStudentsSchema(many=True)
